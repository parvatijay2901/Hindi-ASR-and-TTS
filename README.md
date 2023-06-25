# Hindi-ASR-and-TTS
## Summary
In this project, we have focussed on creating an Automatic Speech Recognition (ASR) and Text to Speech (TTS) module for low resource Indic language Hindi.

![image](https://user-images.githubusercontent.com/51737416/179416806-32458255-3189-4938-8e36-0deee101ac61.png)


The Hindi ASR module was designed using Facebook’s Wav2Vec 2.0 model. Submissions were also made to the ‘GRAM VAANI ASR Challenge 2022’ in the ‘Open’ and ‘self-supervised’ categories. For the open challenge, we have used a pre-trained model by Vakyansh named ‘CLSRIL-23’ and further fine-tuned using 100hrs telephonic labeled data. For the self-supervised challenge, we initially designed a pre-trained model using 1000hrs telephonic unlabeled data and then finetuned using 100hrs telephonic labeled data. A language model, KenLM was used in the decoding step to improve the model’s accuracy.


The Hindi TTS model was developed using Tacotron2 and Parallel WaveGAN models. TTS synthesizer mainly contains two modules, one being 'Spectrogram Prediction Network' and 'Vocoder'. Tacotron2 is an AI-powered end-to-end speech synthesis model developed by Google. It takes processed characters as input and has the ability to convert them to a speech waveform. In our project, we have used the Tacotron2 model to just create the acoustic features for us. The acoustic and spectral features are then fed to a vocoder named ‘Parallel WaveGAN’ where we get speech as the output. Both the models are trained on 21.46hrs IIT Madras Hindi dataset (female voice).

- Project report can be accessed [here](https://docs.google.com/document/d/1ulT7i-4MOYW7guXXULJ9bg0HH9iHOqw22Wb0uDffDYE/edit?usp=sharing).
- Project presentation can be accessed [here](https://docs.google.com/presentation/d/1u3KV-hxQIpWwTwDYy3crKLr3Lfhcydl0aCQyCfMXNsQ/edit?usp=sharing).


