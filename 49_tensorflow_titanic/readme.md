
# Machine learning 13_ MLP with Tensorflow

## In this project I Use Tensorflow library to make a model for titanic dataset.


## titanic dataset:

This dataset has two part:
train and test

I use train part for my project. At fisrt I do a preprocessing on it. Then I select some feature that more useful for classifying and make our result more accurate.
After I select the best features I fit my model that I made it by tensorflow.

Preprocessing:
first I check null sample and I remove rows that has a few null sample.
But 'Age' feature has a lot of null sample, and if I want to remove those rows, I will miss a lot of data. So In Age column I fill null sample with median age value of other person.
I want to use name column too, So I extract just title of each person's name and I create a new column which name is 'title' and I gave a number to each uniqe value in title age. 
I do the same for Sex and Embarks columns.

For cabin column I extract the first character of each person's cabin and then I assigned a numerical value to each unique sample in the cabin column.

I select below 6 features for my model:
'Pclass','Sex','Fare','Cabin','Embarked','Title'

then I creatre my model with below Specifications:

I use two hidden layer.
neuron number of first hidden layer: 36
neuron number of first hidden layer: 18
activation function of fisrt three layers:   relu
activation function of last layer:          softmax
epochs number:      500
optimizer:     Adamax
learning rate: 0.01




## How to install
Run following command :

pip install -r requirements.txt


## How to Run

In each .ipynb file run each block to see the result. 

## Results

Accuracy and loss of training data:

![train_acc](https://github.com/javad7189/python-assignment/assets/86910174/c25c2c24-57f1-4138-877f-83b3f5ed3ede)

![train loss](https://github.com/javad7189/python-assignment/assets/86910174/055d5407-5fc9-4b33-8fb1-08246154bd81)


accuracy and loss of test data:

![test](https://github.com/javad7189/python-assignment/assets/86910174/13d6c7ca-a1a0-4c9f-8dfb-360701e8935a)









