
# Machine learning 14_ MLP or Multi Layer Perceptron for Regression

## In this assignment I've done machine learning course in sololearn and I get its certificate.

## In this project I Use Tensorflow library to make a Regression model for two below dataset.

Weather dataset   
House Price dataset

House Price dataset is existed in Kaggle site and you can download it from below links:


House Price dataset link:          https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data


## Weather dataset:

This dataset has some measured data of each hour of all days of some years from 2006 to 2017.


At first I do a preprocessing on data. Then I select some feature that more useful for Regression model and make our result less loss.
After I select the best features I fit my model that I made it by tensorflow.

Preprocessing:
first I calculate the average temprature of each day and I use average value for each day instead of 24 value for each day. I do this for all other features.
Then I check null sample and I use mean value of other row values of each column for null values of that column.
I also use numeric columns for my model.


I select below 3 features for my model:
'DayOfYear','Visibility (km)','Humidity'

these three features have more correlation with our target 'Temperature (C)'.

then I creatre my model with below Specifications:

I use two hidden layer.
neuron number of input layer: 3
neuron number of first hidden layer: 9
neuron number of second hidden layer: 3
neuron number of output layer: 1
activation function of fisrt three layers:   relu
activation function of last layer:          linear
epochs number:      150
optimizer:     AdamW
learning rate: 0.001

I also compare MLP result with a perceptron result that I calculate it in assignment 47.
You can see the out of of two model beside true data for year 2006 in results part.


## House price dataset:

This dataset has some data about houses specifications.


At first I do a preprocessing on data. Then I select some feature that more useful for Regression model and make our result less loss.
After I select the best features I fit my model that I made it by tensorflow.

Preprocessing:
At fisrt I extract numerice feature and I use them in future calculations.
Then I check null sample and I use mean value of other row values of each column for null values of that column.
Then I calculate correlation and I use features that their correlation with 'Sales Price' are more than 50%. 


I find below 10 features for my model:
['OverallQual', 'YearBuilt', 'YearRemodAdd', 'TotalBsmtSF', '1stFlrSF', 'GrLivArea', 'FullBath', 'TotRmsAbvGrd', 'GarageCars', 'GarageArea']

these 10 features have more correlation with our target 'Sales Price'.

then I creatre my model with below Specifications:

I use two hidden layer.
neuron number of input layer: 10
neuron number of first hidden layer: 40
neuron number of second hidden layer: 20
neuron number of output layer: 1
activation function of fisrt three layers:   relu
activation function of last layer:          linear
epochs number:      50
optimizer:     Adam
learning rate: 0.001

I use my model on Test data of house price from kaggle site and I submit my results for test data on kaggle site.

## How to install
Run following command :

pip install -r requirements.txt


## How to Run

In each .ipynb file run each block to see the result. 

## Results


### Result of weather prediction:


Loss of training data:

![lossoftraindataForweather](https://github.com/javad7189/python-assignment/assets/86910174/2fe6a037-1bb8-4289-bfad-1aea42da5c32)


Loss of test data:

![lossofvalidationdata](https://github.com/javad7189/python-assignment/assets/86910174/93928383-66e4-4832-8d13-a930833e2fa0)


compare MLP and perceptron of assignment 47:

![output](https://github.com/javad7189/python-assignment/assets/86910174/36f219a4-f9af-4754-8bbb-19c974ff04c8)


### Result of House Price prediction:


Loss of training data:

![lossFortraindata](https://github.com/javad7189/python-assignment/assets/86910174/4ada4c3e-2cc3-47b5-b575-8b1c84a62db2)


Loss of test data:

![lossofvalidationdata](https://github.com/javad7189/python-assignment/assets/86910174/c7f714c9-4ebc-43fe-a6e7-e5691a5e28c1)


Price of a house with my house specifications:

![priceofmyhouse](https://github.com/javad7189/python-assignment/assets/86910174/b037ec57-ad5e-44e2-9832-ea7621c495f1)


submission result:

![housepricesubmission](https://github.com/javad7189/python-assignment/assets/86910174/3d4a9bc8-09b7-4e9f-bc23-26913bd91f13)



### certificate of machine learning from sololearn:



link of certificate:

https://api2.sololearn.com/v2/certificates/CC-PYPDAQ1F/image/png


certificate:

![Machine_learning_certificate](https://github.com/javad7189/python-assignment/assets/86910174/f241bce2-7730-4499-bc8e-8b2e9852b3a2)

