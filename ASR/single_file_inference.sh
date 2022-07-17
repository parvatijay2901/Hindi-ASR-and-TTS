dir=$PWD
parentdir="$(dirname "$dir")"
parentdir="$(dirname "$parentdir")"

### Values to change, if any ###
custom_model_path=$parentdir'/checkpoints/custom_model/final_model.pt'
dictionary=$parentdir'/data/finetuning/dict.ltr.txt'
wav_file_path="/home/iiit/Major_project_BJP/ASR/data_eval/audio/audio_wav/audio_5b9f156ad765a1_497786170_88227200_1537152362.wav" # path to single wav file
decoder="kenlm" # viterbi or kenlm
cuda=True
half=False

#If kenlm
lm_name='hindi_lm'
lm_model_path=${parentdir}'/lm/'${lm_name}'/lm.binary'
lexicon_lst_path=${parentdir}'/lm/'${lm_name}'/lexicon.lst'

### Values to change end ###

if [ "$decoder" = "viterbi" ]
then
	python ../../utils/inference/single_file_inference.py -m ${custom_model_path} -d ${dictionary} -w ${wav_file_path} -c ${cuda} -D ${decoder} -H ${half}
else
	python ../../utils/inference/single_file_inference.py -m ${custom_model_path} -d ${dictionary} -w ${wav_file_path} -c ${cuda} -D ${decoder} -H ${half} -l ${lexicon_lst_path} -L ${lm_model_path}
fi
