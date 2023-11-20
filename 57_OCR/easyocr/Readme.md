# Optical Character Recognition - OCR

The first and simplest package for OCR is easyocr.

## Description

I use easyocr to test its power for recognizing english, chinese and persian text in some images.
You can see in result part that the result for English language is good.
Chinese numbers are detected but their confident level is very low.
Persian numbers and charaters are not detected correctly so if you want to detect persian language you should train your own model.

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

|          Image name        | chinese.jpg    | english1.jpg    | english2.jpg    | english3.jpg    | farsi1.jpg    | farsi2.jpg    | farsi3.jpg    |
| :----------------------:   | :---: | :---: |:---: |:---: |:---: |:---: |:---: |
|             Image          |  ![chinese](https://github.com/javadnematollahi/python-assignment/assets/86910174/344a3d32-1e34-4b30-8054-fcdbca07be18) | ![english1](https://github.com/javadnematollahi/python-assignment/assets/86910174/c68747ad-f3d2-4a94-9e81-aff1308e3085)| ![english2](https://github.com/javadnematollahi/python-assignment/assets/86910174/2290bd47-1274-4dfc-a288-6849035e2cdf)| ![english3](https://github.com/javadnematollahi/python-assignment/assets/86910174/ce441309-479f-47cd-ad7c-85af3fe8e6e4)
| ![farsi1](https://github.com/javadnematollahi/python-assignment/assets/86910174/2dc8c2d5-6a75-41bf-bc2a-6ff5905967c9)| ![farsi2](https://github.com/javadnematollahi/python-assignment/assets/86910174/b1904157-74ad-4b6e-a83c-281d5c0c7e59)| ![farsi3](https://github.com/javadnematollahi/python-assignment/assets/86910174/c1f09420-9a62-4f0e-b660-e9a46e0f2868)
  |
| Recognized text from Image | 0 123 45678 9101001000 零 壹  贰  叁  肆  伍  睦  柒  捌  玖 拾 |佰 |仟 | Pz65 PwO   | Y737 XES   | X216 KHB  | ابران
ع ٩ ٥سار
٥ر
  | بر النا
٤٢ ٥٦٧
ب ٩١  | ببر ان
٥٢
٣٣ ٤٦٧   |

 ٤٦٧






