#!/usr/bin/env bash

# Copyright 2021 Peter Wu
#  Apache 2.0  (http://www.apache.org/licenses/LICENSE-2.0)

# shellcheck disable=SC1091
. utils/parse_options.sh

. ./path.sh || exit 1;
. ./cmd.sh || exit 1;
. ./db.sh || exit 1;


g2p=espeak_ng_hindi
#g2p=g2p_en_no_space
nj=4
text_format=phn

text_db=text_db


for dset in "${text_db}"; do
    #utils/copy_data_dir.sh "data/${dset}" "data/${dset}_phn"
    echo "BEGIN ${dset} "
    rm -r ${dset}/text_phn
    pyscripts/utils/convert_text_to_phn.py --g2p "${g2p}" --nj "${nj}" \
        "${dset}/text" "${dset}/text_phn"
    echo "END ${dset} "
    #utils/fix_data_dir.sh "data/${dset}_phn"
done

echo "Successfully created tokens."
