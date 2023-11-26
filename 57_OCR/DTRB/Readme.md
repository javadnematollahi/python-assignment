# Optical Character Recognition - OCR

After easyocr at the second stage I use deep-text-recognition-benchmark github repository to do OCR task.

## Description

There are some pretrained model in this repository so first of all I fit them on persian and english license plate and persian and English handwriting text. The results are not good so I think about training my model on a big persian license plate. In fact I knew that this model is not good for persian language because it's trained just for English language. 

## Links of project

Big persian license plate dataset:

https://github.com/mut-deep/IR-LPR

deep-text-recognition-benchmark(DTRB) repository:

https://github.com/clovaai/deep-text-recognition-benchmark/tree/master

Pretrained models of DTRB:

https://drive.google.com/drive/folders/15WPsuPJDCzhp2SvYZLRj8mAlT3zmoAMW

## How to install

```
pip install -r requirements.txt
```

##  How to run

To run this file you need to upload .... file in google colab and run it. 
You should also read deep-text-recognition-benchmark repository in github to understand better.

# results

Identifying and extracting text from four images that I used them with easyocr. 


|          Image name        |  english1.jpg    | english2.jpg    | farsi1.jpg    | farsi2.jpg    | 
| :----------------------:   | :---: | :---: |:---: |:---: |
|             Image          | ![english1](https://github.com/javadnematollahi/python-assignment/assets/86910174/ae0f2b23-9d15-4979-93c5-b14c64b862c2)| ![english2](https://github.com/javadnematollahi/python-assignment/assets/86910174/a3f2d6e6-e813-446c-a2da-b40be22cc5f0)| ![farsi1](https://github.com/javadnematollahi/python-assignment/assets/86910174/2fcdf53d-43cc-4006-881b-f4bb3bb8d075)| ![farsi2](https://github.com/javadnematollahi/python-assignment/assets/86910174/75f4e310-25c0-4df9-a327-41e6d5f5b986)| 
| Recognized text from Image | ppz65pwo  | intercomentalize | intarvity | scan | 




