# Optical Character Recognition - OCR



## Description

DTRB is not trained on persian language and persian plate. So I used DTRB repository to train a model on persian plates.
I used big persian license plate dataset for training my model. 
At first I should convert dataset to lmdb format and then I give it to model.

I also need to exchange of Persian character to English charater In dataset|

I use below table for this porpuse:

|  English  |  Persian  | English  |  Persian  |  English  |  Persian  |  English  |  Persian  | 
| :-----:   | :-------: | :-----:   | :-------: | :-----:   | :-------: | :-----:   | :-------: |
|  'A'  |   'الف'        |  'D'      | 'D'      |  'V' | 'و' |            '9'  | '۹' |
| 'B'   |  'ب'          |   'S'      | 'S'      |   'H' | 'ه' |         '@'| 'ویلچر' |
|   'P' | 'پ'           |   'J'      | 'ج'      |   'I' | 'ی' |
|   'T' | 'ت'         |  'W'      | 'د'         |   '1' | '۱' |
|   'Y' | 'ث'         |   'C'      | 'س'      |   '2' | '۲' |
|   'Z' | 'ز'         |  'U'      | 'ص'      |  '3'  | '۳' |
|   'X' | 'ش'         |   'R'      | 'ط'      |  '4' | '۴' |
|   'E' | 'ع'         |   'Q'      | 'ق'      |   '5' | '۵' | 
|   'F' | 'ف'         |   'L'      | 'ل'      |   '6' | '۶' |
|   'K' | 'ک'         |  'M'      | 'م'      |   '7' | '۷' |
|   'G' | 'گ'         |   'N'      | 'ن'      | '8' | '۸' |


## Links of project

Big persian license plate dataset:

https://github.com/mut-deep/IR-LPR

deep-text-recognition-benchmark(DTRB) repository:

https://github.com/clovaai/deep-text-recognition-benchmark/tree/master

Pretrained models of DTRB:

https://drive.google.com/drive/folders/15WPsuPJDCzhp2SvYZLRj8mAlT3zmoAMW

link of my trained model for persian plates:

https://drive.google.com/file/d/1-5XdLStsty-bqStg1c36WOUC55CMdkAo/view?usp=drive_link

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

results of training model:


|          |  Accuracy    | 
| :---------:   | :---: | 
|  Train   | 80.578 % |
|  Test | 80.439 % |


Identifying and extracting text from four images that I used them with easyocr. 


|          Image name        |  00022.jpg    | 00085.jpg  | 00192.jpg  | 01640.jpg  |  01656.jpg  | 
| :----------------------:   | :-----------: | :--------: | :--------: |:---------: | :---------: |
|             Image          | ![00022](https://github.com/javadnematollahi/python-assignment/assets/86910174/76bc5ee3-e537-47b5-9886-c88f64245ebc)| ![00085](https://github.com/javadnematollahi/python-assignment/assets/86910174/9f4dddee-9eb6-41e1-9f58-190394c54cc4)| ![00192](https://github.com/javadnematollahi/python-assignment/assets/86910174/ea0e57f6-4c96-489e-8b4a-bf94ce5a0f7e)| ![01640](https://github.com/javadnematollahi/python-assignment/assets/86910174/3a33fcb6-233b-40e5-bdf2-f707f42402ae)| ![01656](https://github.com/javadnematollahi/python-assignment/assets/86910174/5b184fff-b5da-4f84-9453-58130af5b4bf)|
| Recognized text from Image | 28i21255   | 68b31699 | 67e77379 | 28i21255  | 97i48912 |
| Change English to Persian  | ی=i | ب=b |  ع=e | ی=i  | ی=i  |




