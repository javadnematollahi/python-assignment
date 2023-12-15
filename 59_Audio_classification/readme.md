# Voice Classification

In this Project I'm going to work with voices and classify them.

## Description

To work with voice, we need a preprocess step to convert the voices to our custom format. 
What I did in preprocess step is:
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

Run below command in terminal to preprocess voice data:

```
python merge_voices.py
```

Run below command in terminal to merge voices:

```
python merge_voices.py
```


Run below command in terminal to remove silence from voices and convert them to .wav file:

```
python remove_silences_and_to_wav.py
```

Run below command in terminal to split voices to 1 second parts:

```
python split_voices.py
```



