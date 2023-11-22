# Optical Character Recognition - OCR

The first and simplest package for OCR is easyocr.

## Description

I use easyocr to test its power for recognizing english and persian text in some images.
You can see in result part that the result for English language is almost good.
Persian numbers and charaters are not detected correctly on plate so if you want to detect persian number and character you should train your own model.
But in persian handwriting the result is almost good.

## How to install

```
pip install -r requirements.txt
```

##  How to run

Run below command in terminal to create model and train data and save a predicted result of an example picture:

```
python Easy_OCR.py
```

# results

Identifying and extracting text from each image stored in a text file named "image_text.txt."

|          Image name        |  english1.jpg    | english2.jpg    | farsi1.jpg    | farsi2.jpg    | 
| :----------------------:   | :---: | :---: |:---: |:---: |
|             Image          |  ![english1](https://github.com/javadnematollahi/python-assignment/assets/86910174/c946ecf8-bca8-4044-bf71-33c40f958d31)| ![english2](https://github.com/javadnematollahi/python-assignment/assets/86910174/e016b771-38f1-497e-a35b-551f647e1942)| ![farsi1](https://github.com/javadnematollahi/python-assignment/assets/86910174/02fdd9d8-4ad5-458f-b08f-cb793dc3ab77)| ![farsi2](https://github.com/javadnematollahi/python-assignment/assets/86910174/a7785c6e-c0aa-4688-8a04-16e4d7c6d36a)| 
| Recognized text from Image | Pz65 PwO  | Bveyyday may nEbe buk Hhee is in cgood somelhing joodL Gluday |بر النا٤٢ ٥٦٧ب ٩١| مولانا صدنامه فرستادم صدراهنشان دادم یاراه یوانی یانامم ئی خوانی | 






