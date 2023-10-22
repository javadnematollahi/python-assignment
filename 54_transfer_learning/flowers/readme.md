# Transfer Learning 

The problem in this part was about increasing accuray of model. I solved this problem by using ready models.
In fact there is a method that you can use ready models that was trained on imagenet dataset with 1000 classes. The point is when you intend to use these models, you'd better drop top layers and made your own Dense layers and output layer.

There are a lot of model in tensorflow library that you can find them in below link:

https://www.tensorflow.org/api_docs/python/tf/keras/applications

## Description

For flowers dataset I use RegNetX032 model.

### Flowers Dataset:

Flowers dataset include 17 kind of flowers.

1. I use this dataset in session 53, so I compare the new result with last result without using transfer learning. 

Results of my model and RegNetX032 model are shown in below table::
 
 |           |       Loss     |        accuracy     |
 |---------: | :----------------: |:----------------: |
 |    Train            |       0.7134            |        0.7451          |
 |    Train(transfer learning)       |        0.0448          |        0.9912          |
 |    Validation            |       1.1493            |        0.6765          |
 |    Validation (transfer learning)      |        0.4053          |        0.9118           |


## How to install

```
pip install -r requirements.txt
```

##  How to run

Run below command in terminal to create model and train data :

```
flowers.py
```

Point:   If you don't have GPU on your system, I recommend to use google colab for running this file. 
