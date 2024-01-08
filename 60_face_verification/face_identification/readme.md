# Face Identification

Let's made a face identification with insightface.

## Description

First of all I made a face bank with pictures of faces that I want to identify them.

Then I made a face identifier.

As I said I used insightface package for extract face features.

## Links of project

Link of insight face github:

https://github.com/deepinsight/insightface

## How to install

```
pip install -r requirements.txt
```

##  How to run

Run Below command in terminal to create face_bank.npy file:

```
python creat_face_bank.py
```


Run Below command in terminal for identifying faces in an image:

```
python face_identification.py --image enter/image/path
```

Run Below command in terminal for identifying faces in an image and update the facebank.npy file automatically:

```
python face_identification.py --update --image enter/image/path
```
In fact you can add some photos to face_bank directory and update facebank.npy file by using top command.

Run Below command in terminal for identifying faces in an image and save the result:

```
python face_identification.py --image enter/image/path --save True
```
# results









