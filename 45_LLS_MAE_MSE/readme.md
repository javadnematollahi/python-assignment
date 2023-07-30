
# Machine learning 8_ LLS

In this project we try to analyze the price of tehran houses and the price of dollar in 3 presidency in Iran.

We use LLs algorithm. LLS or linear least sqaure is a regression algorithm and it is useful for solving linear problem.




## fisrt problem:

### train_test_split

There is a method In scikit learn library for split data to train and test.
In first problem I rewrite this function in train_test_split.py file. 
I define a class which name is TTS that get X and Y and spplit them to train and test.
you can also define the size of train and test data.

## second problem:

### Tehran house-prices

In the second problem I survey the tehran house price. There is a dataset which collect by mohamadreza kariminezhad and you can
access it from below link:

https://www.kaggle.com/mokar2001/house-price-tehran-iran

I preprocess this dataset to delete duplicate rows and null values.

Then I get the price of 5 most expensive house in tehran.
then I alculate the correlation matric for features and I use the features that have most correlation with price.
And then I fit these features and the price columns to LLs algorithm as train and test respectivily. 

## Third problem:

### Dollar house-prices

In the third problem I survey the Dollar price in 3 presidency. There is a dataset which collect by Taghizadeh from tgju.org site and you can
access it from below link:

https://github.com/M-Taghizadeh/Dollar_Rial_Price_Dataset

MR taghizadeh put a python code in his github that you can update the price of dollar from tgju.org site so I used this code to update
the price of dollar until july 2023.


I preprocess this dataset to delete duplicate rows.
I divide data to 3 part that each part relate to one of presidency period.
Then I get the max and min price of dollar in 3 presidency and at the end I get MAE for 3 divided dataset.

## How to install
Run following command :

pip install -r requirements.txt


## How to Run

In each .ipynb file run each block to see the result. 

## Results


#### second problem:

The price of 5 most expensive house in tehran:


Results of MY_LLS model and RidgeCV and LinearRegression for tehran house price:




#### third problem:

MAX dollar price:




Min dollar price:




MAE for dollar price:
