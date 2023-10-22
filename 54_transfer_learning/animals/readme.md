# Transfer Learning 

The problem that I could solve in this, was increasing accuray of model. I solved this problem by using ready models.
In fact there is a method that you can use ready models that was trained on imagenet dataset with 1000 classes. The point is when you intend to use these models, you'd better drop top layers and made your own Dense layers and output layer.

There are a lot of model in tensorflow library that you can find them in below link:

https://www.tensorflow.org/api_docs/python/tf/keras/applications

## Description

For animal datasets I use RegNetX032 model.

### Animals Dataset:

Animals dataset has five type of animals.

1. I use this dataset in session 53, so I compare the new result with last result without using transfer learning. 

Results of my model and RegNetX032 model are shown in below table::
 
 |           |       Loss     |        accuracy     |
 |---------: | :----------------: |:----------------: |
 |    Train            |       0.4242            |        0.8375          |
 |    Train(transfer learning)       |        0.1167          |        0.9667           |
 |    Validation            |       0.4242            |        0.8375          |
 |    Validation (transfer learning)      |        0.2015          |        0.9297           |


## How to install

```
pip install -r requirements.txt
```

##  How to run


Run below command in terminal to create model and train data:

```
python animals.py
```

Point:   If you don't have GPU on your system, I recommend to use google colab for running this file. 


