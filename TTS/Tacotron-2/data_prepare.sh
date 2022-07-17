#!/usr/bin/env bash

# Copyright 2021 Peter Wu
#  Apache 2.0  (http://www.apache.org/licenses/LICENSE-2.0)

# shellcheck disable=SC1091
. utils/parse_options.sh

. ./path.sh || exit 1;
. ./cmd.sh || exit 1;
. ./db.sh || exit 1;

train_set=train_no_dev
dev_set=dev
eval_set=eval

# shellcheck disable=SC1091
. utils/parse_options.sh || exit 1;

db=/home/iiit/Hindi_TTS/Indic_hindi_female/wav
spk=hindi_spkr_hindi_lang
rm -r data
[ ! -e data/${spk} ] && mkdir -p data/${spk}

# set filenames
scp=data/${spk}/wav.scp
utt2spk=data/${spk}/utt2spk
text=data/${spk}/text
segments=data/${spk}/segments
spk2utt=data/${spk}/spk2utt
scp1=data/${spk}/wav1.scp
text1=data/${spk}/text1


# make scp, utt2spk, and spk2utt
find ${db} -name "*.wav" -follow | sort | while read -r filename;do
    id="${spk}_$(basename ${filename} | sed -e "s/\.[^\.]*$//g")"
    echo "${id} ${filename}" >> ${scp}
    echo "${id} ${spk}" >> ${utt2spk}
done
echo "Successfully finished making wav.scp, utt2spk."

utils/utt2spk_to_spk2utt.pl ${utt2spk} > ${spk2utt}
echo "Successfully finished making spk2utt."

# make text
raw_text=/home/iiit/Hindi_TTS/Indic_hindi_female/meta/txt.data
ids=$(sed < ${raw_text} -e "s/^/${spk}_/g" -e "s/$//g" | cut -d " " -f 1 | cut -f 1)
sentences=$(sed < ${raw_text} -e "s/^( //g" -e "s/ )$//g" -e "s/\"//g" | awk '{ $1="";print}')
paste -d " " <(echo "${ids}") <(echo "${sentences}") > ${text}
echo "Successfully finished making text."

utils/fix_data_dir.sh data/${spk}
utils/validate_data_dir.sh --no-feats data/${spk}

cd data/${spk}/

paste -d ':' text wav.scp | shuf | awk -v FS=":" '{ print $1 > "text1" ; print $2 > "wav1.scp" }'
rm -r text wav.scp
mv text1 text
mv wav1.scp wav.scp

cd ../../

# split
utils/subset_data_dir.sh --last data/${spk} 200 data/${spk}_tmp
utils/subset_data_dir.sh --last data/${spk}_tmp 100 data/${eval_set}
utils/subset_data_dir.sh --first data/${spk}_tmp 100 data/${dev_set}
n=$(( $(wc -l < data/${spk}/wav.scp) - 200 ))
utils/subset_data_dir.sh --first data/${spk} ${n} data/${train_set}

# remove tmp directories
rm -rf data/${spk}_tmp

g2p=espeak_ng_hindi
#g2p=g2p_en_no_space
nj=4
text_format=phn


for dset in "${train_set}" "${dev_set}" "${eval_set}"; do
    utils/copy_data_dir.sh "data/${dset}" "data/${dset}_phn"
    echo "BEGIN ${dset} "
    pyscripts/utils/convert_text_to_phn.py --g2p "${g2p}" --nj "${nj}" \
        "data/${dset}/text" "data/${dset}_phn/text"
    echo "END ${dset} "
    utils/fix_data_dir.sh "data/${dset}_phn"
done

echo "Successfully prepared data."
