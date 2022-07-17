import glob
import librosa
import numpy as np

filenames = glob.glob("/home/iiit/Major_project_BJP/ASR/data_inference/audio_wav/*.wav") 

#Did not work for .mp3 (audio_mp3/*.mp3)

sr_rates = []
for audio_file in filenames:
	_,sr = librosa.load(audio_file)
	sr_rates.append(sr)
sr_rates = np.unique(sr_rates)
print(sr_rates)
