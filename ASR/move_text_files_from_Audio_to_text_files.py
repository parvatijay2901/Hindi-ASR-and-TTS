import os,glob

files=glob.glob('/home/iiit/Major_project_BJP/ASR/data_finetuning/audio_wav/*.txt')

for f in files:
	os.system('cp '+f+' /home/iiit/Major_project_BJP/ASR/data_finetuning/text_files/')




