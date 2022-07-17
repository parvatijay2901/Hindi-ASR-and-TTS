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

tag_exp = "/home/iiit/Major_project_BJP/Hindi_tts/espnet/egs2/BJP_MajorProject/tts1/exp/tts_train_raw_phn_none/train.loss.ave_5best.pth"
train_config="/home/iiit/Major_project_BJP/Hindi_tts/espnet/egs2/BJP_MajorProject/tts1/exp/tts_train_raw_phn_none/config.yaml"

vocoder_tag = "/home/iiit/Major_project_BJP/Hindi_tts/ParallelWaveGAN/egs/hindi_iitm_female/voc1/exp1/train_nodev_hin_f_iitm/checkpoint-400000steps.pkl"
vocoder_config="/home/iiit/Major_project_BJP/Hindi_tts/ParallelWaveGAN/egs/hindi_iitm_female/voc1/exp1/train_nodev_hin_f_iitm/config.yml"

text2speech = Text2Speech.from_pretrained(
    train_config=train_config,
    model_file=tag_exp,
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

text = "नमस्ते मैं मित्री, एक हुमानोइड रोबोट हूँ. मुझे तिहान आई आई टी हैदराबाद के तकनिकी टीम द्वारा बनाया गया है. मैं आज के अतिथि, माननीय डॉक्टर जीतेन्द्र सिंह, विज्ञान और प्रौद्योगिकी और पृथ्वी विज्ञान राज्य मंत्री, डॉक्टर श्रीवरी चंद्रशेखर, सचिव, डी.एस.टी, भारत सरकार, प्रोफेसर बी एस मूर्ति, डिरेकटर, आईआईटी हैदराबाद, श्री कोठा प्रभाकर रेड्डी, सांसद, मेडक, डॉक्टर बीवीआर मोहन रेड्डी, अध्यक्ष, बीओजी, आईआईटी हैदराबाद, श्री जी. किशन रेड्डी, भारत के उत्तर-पूर्वी क्षेत्र के पर्यटन, संस्कृति और विकास मंत्री और संसद सदस्य, सिकंदराबाद, और आज के कार्यक्रम के सभी प्रतिभागियों का तिहान आई आई टी हैदराबाद में स्वागत करती हूँ."
input_text = get_lex(text)
start = time.time()
wav = text2speech(input_text)["wav"]
rtf = (time.time() - start)
print(f"RTF = {rtf:5f}")
soundfile.write("Hindi_tihan.wav", wav.numpy(), text2speech.fs, "PCM_16")
