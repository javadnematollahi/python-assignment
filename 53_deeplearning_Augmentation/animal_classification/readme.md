# Augmentation before CNN for animals

In this session I've worked on animals dataset.
This dataset has five type of animals.

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