# Voice Classification

In this Project I'm going to work with voices and classify them. Infact, I want to predict singer name of a song.

## Description

To work with voice, we need a preprocess step to convert the voices to our custom format. 
In this project model was trained on 5 singer voices include: ['chavoshi', 'ebi', 'rezasadeghi', 'shadmehr', 'yegane']
What I did in preprocess step is:

0. separate voice of each singer from music
1. merge voices that are belong to one person
2. remove silence from voices
3. convert all voices to .wav format
4. split voices to 1 second parts and save them in newfolder

After preprocess I upload my dataset to my googledrive to use it from google colab

## Links of project

link of dataset before preprocess:

https://drive.google.com/drive/folders/1--j9EhV5tZpePtGvOML2UxBGsswZUbvd?usp=sharing

link of dataset after preprocess

https://drive.google.com/drive/folders/14-TEg2R8AwJ2PRG1Dz-90Yygy15loVrf?usp=sharing

## How to install

```
pip install -r requirements.txt
```

##  How to run

Run below command in terminal to separate music and voice of singer because we just need voice of each singer:

```
python spleeter.py
```


Run below command in terminal for audio classifying:

```
python audio_classification.py
```

