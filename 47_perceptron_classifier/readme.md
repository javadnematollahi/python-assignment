
# Machine learning 10_ perceptron

In this project we try to analyze three dataset with perceptron.

perceptron is an algrithm that use input data and output data to update wieghts.
weights in perceptron are used for calculate outputdata.

There are different formula for update weight in perceptron. In this project we use SDG formula
for updating weights.



# fisrt problem:

## Surgical 

In first problem I've done a classification on surgical database with perceptron.
perceptron algorithm is used for both classification and regression problems.
when we want to use it for classification, we must use an activation function to map our output to numbers that relates to our classes.

There are different activation function that we can use them in different situation for example: logestic(sigmoid),relu,step,tanh,...

At first I write a perceptron class to use it for classifying surgical data. then I fit perceptron class on data.
I use fourty epochs in train step. I plotted loss and accuracy for train and test data.
In first plot I used epochs for x axes and accuracy for y axes.
In second plot I used epochs for x axes and loss for y axes.


then I calculate and plot confusion matric.


I also repeat above steps with 5 another activation functions and I put the results of each functions in result part. 

## second problem:

### weather dataset

weather dataset is the second dataset that I used it to test my perceptron algorithm.
you can access this dataset in input folder.

At first I add another column to dataset for days. In fact I use 'Formatted Date' column to calculate the day number of each rows in a year, for example I use 12
for 2006-01-12 because this date is equal to 12th days in year.
then I calculate the mean temperature of each days in each years. and then I plot the temperature by day number for all years in dataset.

then I used another perceptron class to solve these regression problem. In regression problem we don't need activation function and we cant calculate accuracy.

So I use evaluate function to calculate loss and then I write a predict function that could predict temperature with day number.
for example you give 200 to it as input and it return the temperature of 200th day of year.

Finally I plot wieghts and biases and losses for training steps iterations.


## How to install
Run following command :

pip install -r requirements.txt


## How to Run

In each .ipynb file run each block to see the result. 

## Results

#### first problem:



input length= 24      learning rate w= 0.1        epochs=40

## activation function= sigmoid

Plot accuracy in each epoch for train and test data:

![model accuracy with sigmoid](https://github.com/javad7189/python-assignment/assets/86910174/88a3a84d-f612-44ec-82f1-9e347f3d813f)



Plot loss in each epoch for train and test data:

![model loss with sigmoid](https://github.com/javad7189/python-assignment/assets/86910174/17f7d812-5841-401a-ad86-90d7e8c3e62d)



Plot confusion matric:

![confusion matric with sigmoid](https://github.com/javad7189/python-assignment/assets/86910174/6a53a88d-9d2c-4a2c-8dd4-1fdb02252f6a)



## activation function= relu

Plot accuracy in each epoch for train and test data:

![model accuracy with relu](https://github.com/javad7189/python-assignment/assets/86910174/384a2ef5-1c31-40f8-b9ab-7df3ec1ee42f)



Plot loss in each epoch for train and test data:

![model loss with relu](https://github.com/javad7189/python-assignment/assets/86910174/45742ba3-5e8f-427c-8c2b-1afed192fbfe)



Plot confusion matric:

![confusion matric with relu](https://github.com/javad7189/python-assignment/assets/86910174/916dc6d6-639d-4749-92b4-544f76de2e47)



## activation function= tanh

Plot accuracy in each epoch for train and test data:

![model accuracy with tanh](https://github.com/javad7189/python-assignment/assets/86910174/d59362b7-10e9-4f33-8f3a-a507e3941fdd)



Plot loss in each epoch for train and test data:

![model loss with tanh](https://github.com/javad7189/python-assignment/assets/86910174/e0764c90-0b54-4252-a3c1-56df2a312ad8)



Plot confusion matric:

![confusion matric with tanh](https://github.com/javad7189/python-assignment/assets/86910174/2eef3e51-7cdd-4567-83cb-cacd70b33b36)



## activation function= unitstep

Plot accuracy in each epoch for train and test data:

![model accuracy with unitstep](https://github.com/javad7189/python-assignment/assets/86910174/6ab71988-958c-4ffb-9b24-3d4fe00a30ee)



Plot loss in each epoch for train and test data:

![model loss with unitstep](https://github.com/javad7189/python-assignment/assets/86910174/a36f5145-b808-4165-bf3c-e7f2917bd4ec)



Plot confusion matric:

![confusion matric with unitstep](https://github.com/javad7189/python-assignment/assets/86910174/941a0188-23c1-4727-aa46-e5a216b5d867)



## activation function= sign

Plot accuracy in each epoch for train and test data:

![model accuracy with sign](https://github.com/javad7189/python-assignment/assets/86910174/a784439d-555d-4390-b0d7-f74825f31d14)



Plot loss in each epoch for train and test data:

![model loss with sign](https://github.com/javad7189/python-assignment/assets/86910174/ce4c0303-a06e-4539-a389-64cb3eafbd27)



Plot confusion matric:

![confusion matric with sign](https://github.com/javad7189/python-assignment/assets/86910174/30acd89c-93ca-46fa-8286-8c09c72bed8f)



## activation function= piece-wise-linear

Plot accuracy in each epoch for train and test data:

![model accuracy with piece-wise-linear](https://github.com/javad7189/python-assignment/assets/86910174/b906baef-f41c-4b10-b5ae-49a3a5fec7e3)



Plot loss in each epoch for train and test data:

![model loss with piece-wise-linear](https://github.com/javad7189/python-assignment/assets/86910174/1fa458c2-67a3-4fc4-b882-bd0ad50616fe)



Plot confusion matric:

![confusion matric with piece-wise-linear](https://github.com/javad7189/python-assignment/assets/86910174/bc774454-328c-4640-ad34-69c9987f52bb)



# second problem:

## Table of date and temperature and day number in a year:

![tablefordate_temp_dayofyear](https://github.com/javad7189/python-assignment/assets/86910174/f89d50ed-8e38-4ff5-b177-e45af1d389c5)



## Temperature in different days of 2006 to 2016 years:

![temp_in_different_days](https://github.com/javad7189/python-assignment/assets/86910174/d8d3fc43-2ddd-4f7d-b74e-047845f9942a)


learning rate Wieght= 0.00001      learning rate Bias= 0.0001        epochs=20

## weights and bias and loss for training iteration:

![W-B-L npy](https://github.com/javad7189/python-assignment/assets/86910174/edf5881a-8ff1-4aa3-bb09-5e460ffaf1c8)





