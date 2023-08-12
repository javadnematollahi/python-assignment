
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

 activation function= sigmoid

Plot accuracy in each epoch for train data:



Plot accuracy in each epoch for test data:



Plot confusion matric:



activation function= relu

Plot accuracy in each epoch for train data:



Plot accuracy in each epoch for test data:



Plot confusion matric:



activation function= tanh

Plot accuracy in each epoch for train data:



Plot accuracy in each epoch for test data:



Plot confusion matric:



activation function= unitstep

Plot accuracy in each epoch for train data:



Plot accuracy in each epoch for test data:



Plot confusion matric:



activation function= sign

Plot accuracy in each epoch for train data:



Plot accuracy in each epoch for test data:



Plot confusion matric:



activation function= piece-wise-linear

Plot accuracy in each epoch for train data:



Plot accuracy in each epoch for test data:



Plot confusion matric:


#### second problem:

Table of date and temperature and day number in a year:




Temperature in different days of 2006 to 2016 years:



learning rate Wieght= 0.00001      learning rate Bias= 0.0001        epochs=20



weights and bias and loss for training iteration:





