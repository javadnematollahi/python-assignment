# face verification

Hi again. This project is about face detection and verfication.

## Description

Face verfification is done by helping below repository:

https://github.com/deepinsight/insightface/tree/master/python-package

Infact insightface help us to detect faces and extract the most important feature of human faces.
We can use these features for verifying different persons.

## How to install

```
pip install -r requirements.txt
```

##  How to run


Run below command in terminal:

```
python face_verification.py --image1 "Enter path of the first image" --image2 "Enter path of the second image"
```

## Result

If two input picture are related to same person you will see below text in terminal:
```
   _____                         ____
  / ___/____ _____ ___  ___     / __ \___  ______________  ____  _____
  \__ \/ __ `/ __ `__ \/ _ \   / /_/ / _ \/ ___/ ___/ __ \/ __ \/ ___/
 ___/ / /_/ / / / / / /  __/  / ____/  __/ /  (__  ) /_/ / / / (__  ) 
/____/\__,_/_/ /_/ /_/\___/  /_/    \___/_/  /____/\____/_/ /_/____/ 
```

If two input picture are related to different persons you will see below text in terminal:

```
    ____  _ ________                     __
   / __ \(_) __/ __/__  ________  ____  / /_
  / / / / / /_/ /_/ _ \/ ___/ _ \/ __ \/ __/
 / /_/ / / __/ __/  __/ /  /  __/ / / / /_
/_____/_/_/ /_/  \___/_/   \___/_/ /_/\__/

    ____
   / __ \___  ______________  ____  _____
  / /_/ / _ \/ ___/ ___/ __ \/ __ \/ ___/
 / ____/  __/ /  (__  ) /_/ / / / (__  )
/_/    \___/_/  /____/\____/_/ /_/____/
```
