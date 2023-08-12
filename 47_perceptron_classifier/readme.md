
# Machine learning 10_ perceptron

In this project we try to analyze three dataset with perceptron.

perceptron is an algrithm that use input data and output data to update wieghts.
weights in perceptron are used for calculate outputdata.

There are different formula for update weight in perceptron. In this project we use SDG formula
for updating weights.



## fisrt problem:

### Surgical 

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

![model accuracy with sigmoid](https://github.com/javad7189/python-assignment/assets/86910174/b36d7e74-1be8-450d-842a-319a6093a89f)


Plot loss in each epoch for train and test data:

![model loss with sigmoid](https://github.com/javad7189/python-assignment/assets/86910174/00b58e79-773d-4538-a311-9cecde5b42e0)


Plot confusion matric:

![confusion matric with sigmoid](https://github.com/javad7189/python-assignment/assets/86910174/9f3edd6a-9d15-4a3d-bb18-8c859e56fd51)


## activation function= relu

Plot accuracy in each epoch for train and test data:

![Uploading model accuracy with relu.png…]()


Plot loss in each epoch for train and test data:

![model loss with relu](https://github.com/javad7189/python-assignment/assets/86910174/bed8da8d-07c8-42a5-b12d-9be1b47b9fe7)


Plot confusion matric:

![confusion matric with relu](https://github.com/javad7189/python-assignment/assets/86910174/cda0ee9c-5e2a-4bd0-8016-1a6778d6b10a)


## activation function= tanh

Plot accuracy in each epoch for train and test data:

![model accuracy with tanh](https://github.com/javad7189/python-assignment/assets/86910174/95ff6099-3b38-49e4-a293-aaa91e406658)


Plot loss in each epoch for train and test data:

![model loss with tanh](https://github.com/javad7189/python-assignment/assets/86910174/80f7a859-5400-4f21-afed-5e4fff36f1dd)


Plot confusion matric:

![confusion matric with tanh](https://github.com/javad7189/python-assignment/assets/86910174/998770ce-f7df-4abe-a317-ddffe1d3b0e3)


## activation function= unitstep

Plot accuracy in each epoch for train and test data:

![model accuracy with unitstep](https://github.com/javad7189/python-assignment/assets/86910174/7d2877a9-b3a8-4ea7-9b10-d34b18b77a90)


Plot loss in each epoch for train and test data:

![model loss with unitstep](https://github.com/javad7189/python-assignment/assets/86910174/41ecacec-bbb7-4d35-b186-db414bc21689)


Plot confusion matric:

![confusion matric with unitstep](https://github.com/javad7189/python-assignment/assets/86910174/9d7b9e6d-2398-465d-b560-0779c5e8ba95)


## activation function= sign

Plot accuracy in each epoch for train and test data:

![model accuracy with sign](https://github.com/javad7189/python-assignment/assets/86910174/69bdbc74-836c-4645-95f6-a9f8c84c9b18)


Plot loss in each epoch for train and test data:

![model loss with sign](https://github.com/javad7189/python-assignment/assets/86910174/61eb57ee-1667-4b9e-b770-b5c624462cb4)


Plot confusion matric:

![confusion matric with sign](https://github.com/javad7189/python-assignment/assets/86910174/ddca88ce-6aec-4f75-ad27-1759fcb7c3b2)


## activation function= piece-wise-linear

Plot accuracy in each epoch for train and test data:

![model accuracy with piece-wise-linear](https://github.com/javad7189/python-assignment/assets/86910174/dd157630-0fa9-48d0-97de-98f1279d27c4)


Plot loss in each epoch for train and test data:

![model loss with piece-wise-linear](https://github.com/javad7189/python-assignment/assets/86910174/374524a4-7db8-48b5-96d8-5cb2a1dc5eb2)


Plot confusion matric:

![confusion matric with piece-wise-linear](https://github.com/javad7189/python-assignment/assets/86910174/f4211949-7026-4e0e-8da9-55a62be0881b)


#### second problem:

## Table of date and temperature and day number in a year:

![tablefordate_temp_dayofyear](https://github.com/javad7189/python-assignment/assets/86910174/f89d50ed-8e38-4ff5-b177-e45af1d389c5)



## Temperature in different days of 2006 to 2016 years:

![temp_in_different_days](https://github.com/javad7189/python-assignment/assets/86910174/d8d3fc43-2ddd-4f7d-b74e-047845f9942a)


learning rate Wieght= 0.00001      learning rate Bias= 0.0001        epochs=20

## weights and bias and loss for training iteration:

![W-B-L npy](https://github.com/javad7189/python-assignment/assets/86910174/edf5881a-8ff1-4aa3-bb09-5e460ffaf1c8)





