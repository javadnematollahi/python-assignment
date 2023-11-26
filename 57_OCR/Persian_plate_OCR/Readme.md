# Optical Character Recognition - OCR



## Description

DTRB is not trained on persian language and persian plate. So I used DTRB repository to train a model on persian plates.
I used big persian license plate dataset for training my model. 
At first I should convert dataset to lmdb format and then I give it to model.

I also need to exchange of Persian character to English charater In dataset|

I use below table for this porpuse|

|  English  |  Persian  | 
| :-----:   | :-------: |
|  'A'  |   'الف'  |
| 'B'   |  'ب' |
|   'P' | 'پ' |
|   'T' | 'ت' |
|   'Y' | 'ث' |
|   'Z' | 'ز' |
|   'X' | 'ش' |
|   'E' | 'ع' |
|   'F' | 'ف' |
|   'K' | 'ک' |
|   'G' | 'گ' |
|   'D' | 'D' |
|   'S' | 'S' |
|   'J' | 'ج' |
|   'W' | 'د' |
|   'C' | 'س' |
|   'U' | 'ص' |
|   'R' | 'ط' |
|   'Q' | 'ق' |
|   'L' | 'ل' |
|   'M' | 'م' |
|   'N' | 'ن' |
|   'V' | 'و' |
|   'H' | 'ه' |
|   'I' | 'ی' |
|   '0' | '۰' |
|   '1' | '۱' |
|   '2' | '۲' |
|  '3'  | '۳' |
|   '4' | '۴' |
|   '5' | '۵' | 
|   '6' | '۶' |
|   '7' | '۷' |
|   '8' | '۸' |
|  '9'  | '۹' |
 |         '@'| 'ویلچر'|


## Links of project

Big persian license plate dataset|

https|//github.com/mut-deep/IR-LPR

deep-text-recognition-benchmark(DTRB) repository|

https|//github.com/clovaai/deep-text-recognition-benchmark/tree/master

Pretrained models of DTRB|

https|//drive.google.com/drive/folders/15WPsuPJDCzhp2SvYZLRj8mAlT3zmoAMW

link of my trained model for persian plates|

https|//drive.google.com/file/d/1-5XdLStsty-bqStg1c36WOUC55CMdkAo/view?usp=drive_link

## How to install

```
pip install -r requirements.txt
```

##  How to run

Run Below command in terminal to convert make `.gt` file.

```python convert_XML_gt.py```

To train and test you need to upload DTRB file in google colab and run it. 
You should also read deep-text-recognition-benchmark repository in github to understand better.

# results

results of training model|


|                  |  Accuracy    | 
| :---------:   | :---: | 
|  Train   | 80.578 % |
|  Test | 80.439 % |


Identifying and extracting text from four images that I used them with easyocr. 


|          Image name        |  00022.jpg    | 00085.jpg  | 00192.jpg  | 01640.jpg  |  01656.jpg  | 
| :----------------------:   | :---: | :---: | :---: |:---: |
|             Image          | | | | |  |
| Recognized text from Image | 28i21255   | 68b31699 | 67e77379 | 28i21255  | 97i48912 |
| Change English to Persian | 28ی21255   | 68ب31699 | 67ع77379 | 28ی21255  | 97ی48912 |




