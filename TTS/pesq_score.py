from espnet2.bin.tts_inference import Text2Speech
from espnet2.utils.types import str_or_none
import time
import torch
import soundfile
import glob
import os
import numpy as np
import kaldiio
import subprocess
from convert_text_to_phn_exp import *
from scipy.io import wavfile
from pesq import pesq

tag_exp = "/home/iiit/bhargavi/Hindi_TTS/espnet/egs2/BJP_MajorProject/tts1_try/exp/tts_train_raw_phn_none/train.loss.ave_5best.pth"

train_config= "/home/iiit/bhargavi/Hindi_TTS/espnet/egs2/BJP_MajorProject/tts1_try/exp/tts_train_raw_phn_none/config.yaml"

vocoder_tag = "/home/iiit/bhargavi/ParallelWaveGAN/egs/hindi_iitm_female/voc1/exp/train_nodev_hin_f_iitm/checkpoint-400000steps.pkl"

vocoder_config="/home/iiit/bhargavi/ParallelWaveGAN/egs/hindi_iitm_female/voc1/exp/train_nodev_hin_f_iitm/config.yml"

text2speech = Text2Speech.from_pretrained(
    train_config=train_config,
    model_file=tag_exp,
    vocoder_file=vocoder_tag,
    vocoder_config=vocoder_config,
    device="cpu",
    threshold=0.5,
    minlenratio=0.0,
    maxlenratio=10.0,
    use_att_constraint=True,
    backward_window=1,
    forward_window=3,
    speed_control_alpha=1.0,
    noise_scale=0.333,
    noise_scale_dur=0.333,
    always_fix_seed=False
    )

filenames=glob.glob('./text/*.txt')
list_pesq_scores_wb = []
list_pesq_scores_nb = []

for filename in filenames:
    try:
        text_file = open(filename, 'r')
        text = text_file.read()
        print(filename.split('/')[-1],'--',text)
        input_text = get_lex(text)
        start = time.time()
        wav = text2speech(input_text)["wav"]
        rtf = (time.time() - start)
        #print(f"RTF = {rtf:5f
        
        filename_generated = "./generated_wav/"
        +filename.split('/')[-1][:-3] + "wav"
        soundfile.write(filename_generated, wav.numpy(),
        text2speech.fs, "PCM_16")
        
        filename_wav = "./wav/" + filename.split('/')[-1][:-3] + "wav"
        rate, ref = wavfile.read(filename_wav)
        rate, deg = wavfile.read(filename_generated)
        
        pesq_wb = pesq(rate, ref, deg, 'wb')
        list_pesq_scores_wb.append(pesq_wb)
        print(pesq_wb)
        pesq_nb = pesq(rate, ref, deg, 'nb')
        list_pesq_scores_nb.append(pesq_nb)
        print(pesq_nb)
        
    except:
        print('File not found ', filename.split('/')[-1])
        pass

print("Mean PESQ score (wb):",sum(list_pesq_scores_wb)/len(list_pesq_scores_wb))
print("Mean PESQ score (nb):",sum(list_pesq_scores_nb)/len(list_pesq_scores_nb))
