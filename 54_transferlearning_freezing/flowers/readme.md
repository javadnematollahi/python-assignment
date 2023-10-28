# Transfer Learning and Freeze some layers

We can use transfer learning and Freeze some layers to improve accuracy of our model. 
In fact there is a method that you can use ready models that was trained on imagenet dataset with 1000 classes. The point is when you intend to use these models, you'd better drop top layers and made your own Dense layers and output layer.

There are a lot of model in tensorflow library that you can find them in below link:

https://www.tensorflow.org/api_docs/python/tf/keras/applications

## Description

For flowers dataset I use MobileNet model.

### Flowers Dataset:

Flowers dataset include 17 kind of flowers.

1. I use this dataset in session 53 and 54_1, so I compare the new result with last results. 

Results of simple model and transfer learning model and  transfer learning+freezing are shown in below table::
 
 |           |       Loss     |        accuracy     |
 |---------: | :----------------: |:----------------: |
 |    Train            |       0.7134            |        0.7451          |
 |    Train(transfer learning)       |        0.0448          |        0.9912          |
 |    Train(transfer learning + freezing)       |        0.0030          |        1.0000           |
 |    Validation            |       1.1493            |        0.6765          |
 |    Validation (transfer learning)      |        0.4053          |        0.9118           |
 |    Validation (transfer learning + freezing)      |        0.1679          |        0.9529           |


## How to install

```
pip install -r requirements.txt
```

##  How to run

Run below command in terminal to create model and train data :

```
flowers.py
```

Point:   If you don't have GPU on your system, I recommend to use google colab for running this file.  you should create an account in wandb,too.

## Results

### Loss and Accuracy of train and test

![accuracyandloss_flower](https://github.com/javadnematollahi/python-assignment/assets/86910174/8ae9f1e4-454d-4458-a4a5-2ee18f2af2e8)


### you can see different diagrams of model in below wandb site link:

https://wandb.ai/javad7189/flowers
