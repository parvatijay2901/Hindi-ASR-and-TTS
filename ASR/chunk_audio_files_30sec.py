from pydub import AudioSegment
from pydub.utils import make_chunks
import glob

filenames=glob.glob('/media/iiit/Seagate Backup Plus Drive/BJP/database/Audio/*.wav')
dest_path='/home/iiit/Major_project_BJP/ASR/data_pretraining_audio_wav/'


print(filenames)
number=0
for filename in filenames:
    number=number+1
    myaudio = AudioSegment.from_file (filename, "wav") 
    chunk_length_ms = 30000 # pydub calculates in millisec
    chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec
    l=filename.split('/')
    filename=l[-1][:-4]


    #Export all of the individual chunks as wav files

    for i, chunk in enumerate(chunks):
        chunk_name = "chunk{0}.wav".format(i)
        chunk_name=dest_path+filename+'_' +chunk_name
        print("exporting", chunk_name)
        chunk.export(chunk_name, format="wav")
        
print('Total number of files =',number)
