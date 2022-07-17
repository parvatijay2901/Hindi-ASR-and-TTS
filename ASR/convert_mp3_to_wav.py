import os,glob

filenames=glob.glob('/home/iiit/Major_project_BJP/ASR/data_eval/audio_mp3/*.mp3')

os.system('mkdir /home/iiit/Major_project_BJP/ASR/data_eval/audio_wav')

for file in filenames:
	os.system('ffmpeg -i '+file+' -ar 16000 -ac 1 '+file[:-3]+'wav')
	
os.system('mv /home/iiit/Major_project_BJP/ASR/data_eval/audio_mp3/*.wav /home/iiit/Major_project_BJP/ASR/data_eval/audio_wav/')

