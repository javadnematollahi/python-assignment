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

|          Image name        | chinese.jpg    | #2    |
| :----------------------:   | :---: | :---: |
|             Image          |    | 283   |
| Recognized text from Image | 301   | 283   |

chinese.jpg:
0
123 45678 9
101001000
零 壹  贰  叁  肆  伍  睦  柒  捌  玖 拾 |佰 |仟

english1.jpg:
Pz65 PwO

english2.jpg:
Y737 XES

english3.jpg:
X216 KHB

farsi1.jpg:
ابران
ع ٩ ٥سار
٥ر

farsi2.jpg:
بر النا
٤٢ ٥٦٧
ب ٩١

farsi3.jpg:
ببر ان
٥٢
٣٣ ٤٦٧






