from glob import glob

mp3_files =  open('/home/iiit/Major_project_BJP/ASR/data_eval/script_files/mp3.scp','r').read().split('\n')[:-1]

output_texts =  open('/home/iiit/Major_project_BJP/ASR/data_eval/results_generated/filename_text.txt','r').read().split('\n')[:-1]

#print(len(mp3_files))

#print(len(output_texts))

for f in mp3_files:
	f = f.split('\t')
	for f1 in output_texts:
		f1 = f1.split('\t')
		if f[1].split('/')[-1][:-3] == f1[0][:-3]:
			filename=open('results_using_pretrained.txt','a')
			filename.write(f[0])
			filename.write(' ')
			filename.write(f1[1])
			filename.write('\n')
			filename.close()
