# License Plate Detector 

I have made a license plate identifier and license plate verifier in this project.
I used YOLOv8 for plate detection and I used deep-text-recognition-benchmark repository for text recognizer.

## Description

For both license plate identification and verification I need to do two process.

1. At first I should detect plates in an image.
2. Second I should recognize the texts which were written on each plate.

After doing two top imprtant process, I can use the output of second step for plate identification.

In the next step I used a database of some plates and I checked the plates in each image and compare them with database plates to check their similarity.
If their similarity be bigger than 80%, I return True. 


## Links of project

Big persian license plate dataset used for training YOLOv8 pretrained weights for plate detection:

https://github.com/mut-deep/IR-LPR

deep-text-recognition-benchmark(DTRB) repository:

https://github.com/clovaai/deep-text-recognition-benchmark/tree/master

Pretrained models of deep-text-recognition-benchmark(DTRB):

https://drive.google.com/drive/folders/15WPsuPJDCzhp2SvYZLRj8mAlT3zmoAMW

link of my trained model for recognizing text from persian plates:

https://drive.google.com/file/d/1Te2iZCCIkAxt_Vi-woVH9IJXFlgAWjYU/view?usp=sharing

link of my trained model for detection plates:

https://drive.google.com/file/d/1uE8o9thgaozdEqi_8jqh9kFrFa_OLqMr/view?usp=sharing

## How to install

```
pip install -r requirements.txt
```

##  How to run

Run Below command in terminal for license plate identification:

```python identification.py```


Run Below command in terminal for license plate verification:

```python verification.py```

# results

results of license plate verification:

If you look at fourth column in below picture you can see the result of plate verification as True and False.

In first row my code return True because this plate was defined in my database but other rows have False because they weren't defined in database.

![Verification](https://github.com/javadnematollahi/python-assignment/assets/86910174/594dcfa9-da57-49de-8b46-7050c5ad5288)






