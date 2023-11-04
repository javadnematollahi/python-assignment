# Transfer Learning and Freeze some layers

We can use transfer learning and Freeze some layers to improve accuracy of our model. 
In fact there is a method that you can use ready models that was trained on imagenet dataset with 1000 classes. The point is when you intend to use these models, you must drop top layers and made your own Dense layers and output layer.

There are a lot of model in tensorflow library that you can find them in below link:

https://www.tensorflow.org/api_docs/python/tf/keras/applications

## Description

For 7-7 datasets I use MobileNet model.
This dataset has faces pictures of 14 celebrities.

### 7-7 Dataset:
 
 Accuracy and Loss for transfer learning from 54_1 and transfer learning + freezing:

 |           |       Loss     |        accuracy     |
 |---------: | :----------------: |:----------------: |
 |    Train(transfer learning)       |        0.0826          |        0.9756          |
 |    Train(transfer learning + freezing)       |        0.0003          |        1.0000           |
 |    Validation (transfer learning)      |        0.3150          |        0.9084           |
 |    Validation (transfer learning + freezing)      |        0.2369          |        0.9389           |


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

Run below command in terminal to predict some test images with created model:

```
python predict.py
```
## Results

### loss and accuracy of train and test:

![lossandaccuracy7-7](https://github.com/javadnematollahi/python-assignment/assets/86910174/5be8203c-6058-46e8-9402-43df7d5d14c1)


### confusion matric:

![confusion7-7](https://github.com/javadnematollahi/python-assignment/assets/86910174/15d0893f-df23-4c0d-8862-6bbf4ac033ee)

### Predict of 14 test images

![predict7-7](https://github.com/javadnematollahi/python-assignment/assets/86910174/b097ff86-45ab-4d48-92bd-939106803c4e)


### you can see different diagrams of model in below wandb site link:

https://wandb.ai/javad7189/7-7faces

