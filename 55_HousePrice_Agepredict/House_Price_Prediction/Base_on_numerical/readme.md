# House Price prediction

In this project I want to predict your House Price!

## Description

Dataset Address:

https://github.com/emanhamed/Houses-dataset


There are a lot of model in tensorflow library that you can find them in below link:

https://www.tensorflow.org/api_docs/python/tf/keras/applications


## How to install

```
pip install -r requirements.txt
```

##  How to run

Run below command in terminal to create model and train data and finally print loss of validation data:

```
python load_train_Houseprice.py
```

Run below command in terminal to predict the age of an input picture:

```
python Predict_price.py
```

## Results:

### loss of train and test:

 |           |       Loss(mean_absolute_percentage_error)     |   
 |---------: | :----------------: |
 |    Train     |        25.4789%          |     
 |    Validation    |       28.2502%          |    


### you can see different diagrams of model in below wandb site link:

https://wandb.ai/javad7189/House_price_by_numerical

### Result of model on my own house:

![price_base_on_numerical](https://github.com/javadnematollahi/python-assignment/assets/86910174/b252f785-59d4-4a63-aa74-ef96ab7f21e8)
