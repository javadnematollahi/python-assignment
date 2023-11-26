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
|             Image          | | | | | 
| Recognized text from Image | ppz65pwo  | intercomentalize | intarvity | scan | 




