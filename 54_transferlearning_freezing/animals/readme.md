# Transfer Learning and Freeze some layers

We can use transfer learning and Freeze some layers to improve accuracy of our model. 
In fact there is a method that you can use ready models that was trained on imagenet dataset with 1000 classes. The point is when you intend to use these models, you must drop top layers and made your own Dense layers and output layer. You could also freeze some layers to get better accuracy.

There are a lot of model in tensorflow library that you can find them in below link:

https://www.tensorflow.org/api_docs/python/tf/keras/applications

## Description

For animal datasets I use MobileNetV2 model.

### Animals Dataset:

Animals dataset has five type of animals.

1. I use this dataset in session 53 and 54_1, so I compare the new result with last results. 

Results of simple model and transferlearning model and transferlearning model with freezing are shown in below table:
 
 |           |       Loss     |        accuracy     |
 |---------: | :----------------: |:----------------: |
 |    Train            |       0.4242            |        0.8375          |
 |    Train(transfer learning)       |        0.1167          |        0.9667           |
  |    Train(transfer learning + freezing)       |        0.0025          |        1.0000           |
 |    Validation            |       0.4242            |        0.8375          |
 |    Validation (transfer learning)      |        0.2015          |        0.9297           |
  |    Validation (transfer learning + freezing)      |        0.0644          |        0.9766           |


## How to install

```
pip install -r requirements.txt
```

##  How to run


Run below command in terminal to create model and train data:

```
python animals.py
```

Point:   If you don't have GPU on your system, I recommend to use google colab for running this file. you should create an account in wandb,too.

## Results

### Loss and Accuracy of train and test

![lossandaccuracy_animal](https://github.com/javadnematollahi/python-assignment/assets/86910174/e5a32ec2-a319-41c5-a837-1f464bd6f4fd)


### you can see different diagrams of model in below wandb site link:

https://wandb.ai/javad7189/animals
