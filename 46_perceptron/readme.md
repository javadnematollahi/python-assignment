
# Machine learning 9_ perceptron

In this project we try to analyze three dataset with perceptron.

perceptron is an algrithm that use input data and output data to update wieghts.
weights in perceptron are used for calculate outputdata.

There are different formula for update weight in perceptron. In this project we use SDG formula
for updating weights.



## fisrt problem:

### Employee's salary 

In first problem I used make_regression to produce a dataset for Employee's salary.
After creating this dataset ,I could predict the salary from the given experience, because the relation between salary and experience is linear.

I write a perceptron class in the next step to use it for predicting salary from experience.

I also change the hyperparameter of perceptron class to fit the est line on my dataset.
I draw two diagram, one for data and the line that trough all data and other for loss.

I used MAE method to find loss in this problem.


## second problem:

### Abalone dataset

Abalone dataset is the second dataset that I used it to test my perceptron algorithm.
you can access this dataset from below link:

https://www.kaggle.com/datasets/rodolfomendes/abalone-dataset

At first I split this dataset to train and test. then I used train data to fit my perceptron. and then I find best line 
to fit on this dataset and I find loss in each epoch to survey the functionality of perceptron in each step.
I draw two diagram, one for data and the line that trough all data and other for loss.

I used MAE method to find loss in this problem.


## Third problem:

### Boston house-prices

In the third problem I survey the Boston house price again, but this time I use perceptron.
you can access this dataset from below link:

https://www.kaggle.com/datasets/vikrishnan/boston-house-prices

I find two features that are most related to price of houses and use them to create X_train and used price to create Y_train.

I fit train data to my perceptron algorithm and I also set hyperparameter, then I found out that below value are best for hyperparameter:
learning rate Wieght= 0.0001
learning rate Bias= 0.1
epochs=120

## How to install
Run following command :

pip install -r requirements.txt


## How to Run

In each .ipynb file run each block to see the result. 

## Results

#### first problem:

left diagram is shown Employee's salary data and the line that I find by using perceptron.
right diagram is shown loss value that is calculated in each epochs wth MAE method.

learning rate Wieght= 0.0001      learning rate Bias= 0.1        epochs=4



learning rate Wieght= 0.0001      learning rate Bias= 0.1        epochs=25



#### second problem:

LEFT diagram is shown abalone length and height data and the line that I find by using perceptron.
Right diagram is shown loss value that is claculated in each epochs wth MAE method.


learning rate Wieght= 0.001      learning rate Bias= 0.1        epochs=4



learning rate Wieght= 0.1      learning rate Bias= 0.1        epochs=25



#### third problem:

3D animation of Boston house price and the best plane that fit on these data.

learning rate Wieght= 0.0001      learning rate Bias= 0.1        epochs=120

I show from first step that perceptron started to run to final step that perceptron find the best plane that trough all data.




another 3D animation of the best plane that perceptron could find in 120 epochs.

