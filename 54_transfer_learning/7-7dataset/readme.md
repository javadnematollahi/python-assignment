# Transfer Learning 

The problem that I could solve it, was increasing accuray of model. I solved this problem by using ready models.
In fact there is a method that you can use ready models that was trained on imagenet dataset with 1000 classes. The point is when you intend to use these models, you'd better drop top layers and made your own Dense layers and output layer.

There are a lot of model in tensorflow library that you can find them in below link:

https://www.tensorflow.org/api_docs/python/tf/keras/applications

## Description

For 7-7 datasets I use RegNetX032 model.
This dataset has faces pictures of 14 celebrities.

### 7-7 Dataset:
 
 Accuracy and Loss:

 |           |       Loss     |        accuracy     |
 |---------: | :----------------: |:----------------: |
 |    Train(transfer learning)       |        0.0826          |        0.9756          |
 |    Validation (transfer learning)      |        0.3150          |        0.9084           |

loss and accuracy of train and test:


confusion matric:


result for predicting 14 test images:


## How to install

```
pip install -r requirements.txt
```

##  How to run

Run below command in terminal to create model and train data and finally plot accuracy and loss for epochs:

```
python 7-7dataset.py
```

Run below command in terminal to plot confusion matric:

```
python confusion_matric.py
```

Run below command in terminal to predict some test images with created mdel:

```
python predict.py
```
