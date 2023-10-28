# Transfer Learning and Freeze some layers

We can use transfer learning and Freeze some layers to improve accuracy of our model. 
In fact there is a method that you can use ready models that was trained on imagenet dataset with 1000 classes. The point is when you intend to use these models, you must drop top layers and made your own Dense layers and output layer.

There are a lot of model in tensorflow library that you can find them in below link:

https://www.tensorflow.org/api_docs/python/tf/keras/applications

## Description

For Akhund and Human datasets I use MobileNet model.
This dataset has faces pictures of Akhunds and Humans.

### Akhund and Human Dataset:
 
 Accuracy and Loss for transfer learning from 54_1 and transfer learning + freezing:

 |           |       Loss     |        accuracy     |
 |---------: | :----------------: |:----------------: |
 |    Train(transfer learning)       |        0.0826          |        0.9756          |
 |    Train(transfer learning + freezing)       |        0.1610        |        94.74          |
 |    Validation (transfer learning)      |        0.3150          |        0.9084           |
 |    Validation (transfer learning + freezing)      |        0.2718          |        0.9556           |

## How to install

```
pip install -r requirements.txt
```

##  How to run

Run below command in terminal to create model and train data and finally plot accuracy and loss for epochs:

```
python Akhund_and_Human.py
```

Run below command in terminal to plot confusion matric:

```
python confusion_matric.py
```

Run below command in terminal to run telegram bot for predicting akhund and human:

```
python telegrambot_classification.py
```

## Results:

### loss and accuracy of train and test:


### confusion matric:


### you can see different diagrams of model in below wandb site link: