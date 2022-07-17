import glob
import librosa
import numpy as np

filenames = glob.glob("/home/iiit/Major_project_BJP/ASR/data_inference/audio_wav/*.wav") 

#Did not work for .mp3 (audio_mp3/*.mp3)

#print(len(filenames))

sr_rates = []
for audio_file in filenames:
	_,sr = librosa.load(audio_file)
	sr_rates.append(sr)
sr_rates = np.unique(sr_rates)
print(sr_rates)


#sr_rates = []
#count = 0
#for audio_file in filenames:
#	try:
#		_,sr = librosa.load(audio_file)
#		sr_rates.append(sr)
#	except:
#		count = count + 1

#sr_rates = np.unique(sr_rates)

#print(sr_rates)
#print(count)	
