# Augmentation before CNN 

In this session I've worked on two dataset.
First one has five type of animals and The second one include 17 kind of flower.

The problem that I should solve is ooverfitting. I solve this problem by using Augmentation.
Augmentation is about increasing primary dataset with some techniques.

## Description

### Animals Dataset:

1. There are two python file in animals folder. The file which name is `Animals_CNN_Augmentation.py` is made for creating train and validation data and making model.

2. You can download the created model from below link:

 https://drive.google.com/file/d/1PBpGmPeWEVeRv1xmueKpIDyehaJY8cv-/view?usp=drive_link
 
3. You can access animal dataset from below link:

https://drive.google.com/drive/folders/1wBUlG3P8YBiB17aUo3O6byzO0DJLcsaS?usp=drive_link

Results of my model is shown in below table::
 
 |           |       Loss     |        accuracy     |
 |---------: | :----------------: |:----------------: |
 |    Train            |       0.4242            |        0.8375          |
 |    Validation            |        0.8812          |        0.7000           |

Confusion Matric :

![confusionmatric_animal](https://github.com/javadnematollahi/python-assignment/assets/86910174/7bfe6428-c078-4935-8c06-b316a92a101c)


2. The name of other python file is `animal_predict.py` and is written for predicting some test pictures which are in test folder.

### Flowers Dataset:

   There are three python file in flowers folder. 

A.   The file which name is `flower_classify.py` is made for creating train and validation data and making model. The created model is saved as `flower.h5`. 

 You can download the created model from below link:

 https://drive.google.com/file/d/1C14WJQbNA83BBSB8lGkgqS9mwlsld4Vr/view?usp=drive_link

You can access flower dataset from below link:

https://drive.google.com/drive/folders/1GAFDuS9dcBxYi4MlMwpHUW5Z50Q01k3y

Results of flower.h5 model is shown in below table::
 
 |               |       Loss     |      accuracy    |
 |-------------: | :------------: |:----------------:|
 |    Train      |       0.0067   |       1.0000    |
 |    Validation |       1.5855  |        0.7059    |  

Confusion Matric for flower.h5 model:

![confusionmatric_flower](https://github.com/javadnematollahi/python-assignment/assets/86910174/18952edb-256d-4012-aefe-169403df172a)


B.   The file which name is `flower_classify_Aug.py` is made for creating train and validation data and making model. Furtermore I use Augmentation technique in this file to prevent overfitting. The created model is saved as `flower_aug.h5`. 

 You can download the created model from below link:

 https://drive.google.com/file/d/1iU7IWD1vpGw3xW_hfRtRtxxVxTjsUNx-/view?usp=drive_link

Results of flower_aug.h5 model is shown in below table::
 
 |               |       Loss     |      accuracy    |
 |-------------: | :------------: |:----------------:|
 |    Train      |       0.7134   |        0.7451    |
 |    Validation |        1.1493  |        0.6765    |  

Confusion Matric for flower_aug.h5 model :

![confusionmatric_floweraug](https://github.com/javadnematollahi/python-assignment/assets/86910174/408cf54f-3509-43ce-8fe2-f5ab0a542e6f)


C.   The file which name is `telegrambot_classification.py` is made for creating a telegram bot. You can access this telegram bot with this name:
   @NEW_pylearn_bot

   I use a free host to upload and run my code on it so not to need run this file on your system to use telegram bot.
   This telegram bot has some commands that I wrote them befor and now I add /image command. After send this command, you should send a flower picture and the bot is predicting the name your flower.

## How to install

```
pip install -r requirements.txt
```

##  How to run

1. Go to animal_classification folder.
Run below command in terminal to create model and train data:

```
python Animals_CNN_Augmentation.py
```

Run below command in terminal to predict some new images in test folder:

```
python animal_predict.py
```

1. Go to flower_classification folder.
Run below command in terminal to create model without augmentation and train data :

```
flower_classify.py
```

Run below command in terminal to create model with augmentation and train data :

```
flower_classify_Aug.py
```

Run below command in terminal to run telegram bot and use it for predicting flower image :

```
telegrambot_classification.py
```

As I upload `telegrambot_classification.py` on a server, you can use telegram bot without runnig this code.

