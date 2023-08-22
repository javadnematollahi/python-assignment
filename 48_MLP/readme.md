
# Machine learning 12_ MLP or Multi Layer Perceptron

## In this project I write a class to implement a multilayer perceptron.


I use this class to classify digit numbers from digit_number_dataset which exist in scikit_learn library.

## In fact At first I write a simple multi layer perceptron in an ipynb file then I convert it to class.


this file :   simple_MLP_digitnumbers_data.ipynb (simple mlp)         convert to  ==>        mlp.py(MLP class -OOP)



## In next part I write a OneHotEncoder and a OneHotDecoder function from scratch and I compare my functions results to scikit learn functions results.
## My functions results are similar to Scikit learn results.

In this file I write my own onehotencoder class:  ===>  onehotEncoder.py

## Then I implement fit, evaluate and predict methods of my Mlp class on digits dataset.

this file   ===>  fit_evaluate_predict.ipynb

## After that I write 0 to 9 numbers in separate file and give them to pridect method of my MLP class. The handwriting numbers that I create are in input folder.
## You can see the result in result part.

In this file I predict handwriting numbers by mlp class  ===>  fit_evaluate_predict.ipynb

## I also calculate loss and accuracy by using evaluate method of MLP class.    ===>  fit_evaluate_predict.ipynb

## And Then I plot loss and acuuracy of train data for all epochs during train.     ===>  fit_evaluate_predict.ipynb




## How to install
Run following command :

pip install -r requirements.txt


## How to Run

In each .ipynb file run each block to see the result. 

## Results

Compare the result of onehotencoder and onehotdecoder functions:

![onehotencoder_compare](https://github.com/javad7189/python-assignment/assets/86910174/bafcd45f-c8a0-4675-a101-0fdbf4d3d822)


MLP predict of handwriting numbers :

![handwriting_numbers_test](https://github.com/javad7189/python-assignment/assets/86910174/db5b1a85-328f-4ef0-8dcb-3cfdde2c3119)


Loss and Accuracy of train and test data:

![loss_accuracy_test_train](https://github.com/javad7189/python-assignment/assets/86910174/faf53d92-af63-46dc-b3a5-19d13280fd77)


Loss and Accuracy of train data for all epochs in training phase:

![loss_and_accuracy](https://github.com/javad7189/python-assignment/assets/86910174/e5ddf86a-fb71-4f77-a6cb-54bf95c9653a)



