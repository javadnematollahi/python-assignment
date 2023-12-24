# Voice Classification

In this Project I'm going to work with voices and classify them. Infact, I want to predict singer name of a song.

## Description

To work with voice, we need a preprocess step to convert the voices to our custom format. 

What I did in preprocess step is:

0. separate voice of each singer from music
1. merge voices that are belong to one person
2. remove silence from voices
3. convert all voices to .wav format
4. split voices to 1 second parts and save them in newfolder

After preprocess I upload my dataset to my googledrive to use it from google colab

## Links of project

link of dataset before preprocess:



link of dataset after preprocess



## How to install

```
pip install -r requirements.txt
```

##  How to run

Run below command in terminal to separate music and voice of singer because we just want to use voice of each singer:

```
python spleeter.py
```
Run below command in terminal to preprocess voice data:

```
python preprocess.py
```
In preprocess below process is done:

1. merge voices  =>  merge_voices.py
2. remove silence from voices and convert them to .wav file  => remove_silences_and_to_wav.py
3. split voices to 1 second parts and then use them for training model  =>  split_voices.py

Run below command in terminal to train model:

```
python train_singer_model.py
```

Run below command in terminal to inference model:

```
python inference_singer_voices.py
```
