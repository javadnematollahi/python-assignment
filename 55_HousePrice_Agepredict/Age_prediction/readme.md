# Age prediction

In this project I want to predict your age!

## Description

Dataset Address:

https://susanqq.github.io/UTKFace/

OR

https://www.kaggle.com/datasets/jangedoo/utkface-new

Pretrained model that I use for this model:

MobileNet

There are a lot of model in tensorflow library that you can find them in below link:

https://www.tensorflow.org/api_docs/python/tf/keras/applications


## How to install

```
pip install -r requirements.txt
```

##  How to run

Run below command in terminal to create model and train data and finally print loss of validation data:

```
python load_train_age_model.py
```

Run below command in terminal to predict the age of an input picture:

```
python Age_prediction.py
```

## Results:

### loss of train and test:

 |           |       Loss     |   
 |---------: | :----------------: |
 |    Train     |        4.2915          |     
 |    Validation    |        6.0586          |    


### you can see different diagrams of model in below wandb site link:

https://wandb.ai/javad7189/Age_detection

### Result of model on my own picture

