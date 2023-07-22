
# Machine learning 6_ Finding Nemo

In this section we solve a classification problem to separate a predefined object from its background.

The algorithm that we use is KNN that we write as KNN class in myknn.
you can import it by this way:
from myknn import KNN


## fisrt problem:

### Finding nemo

I use KNN algorithm for two classes which include nemo and background.
I use a picture of nemo for training. 
At first, In this picture, I use opencv library to separate nemo pixels from its background.
Then I use nemo pixels as first class and background pixels as second class and I made a trainng data with these two class.
The features are Hue, Sturation and Value of each pixel.

In the next step I made a label matric for training data.


Then I fit KNN with train data.

After that I give a new picture of nemo family to my algorithm and the out put of algorithm is a picture that inculde just the family member of nemo without background.

At the end I made a finding nemo class that get a family member of nemo and return that picture include family member of nemo without background.

## second problem:

### Finding dori

I use KNN algorithm for two classes which include dori and background.
I use a picture of dori for training. 
At first, In this picture, I use opencv library to separate dori pixels from its background.
Then I use dori pixels as first class and background pixels as second class and I made a trainng data with these two class.
The features are Hue, Sturation and Value of each pixel.

In the next step I made a label matric for training data.


Then I fit KNN with train data.

After that I give a new picture of dori family to my algorithm and the out put of algorithm is a picture that inculde just the family member of dori without background.

At the end I made a finding dori class that get a family member of dori and return that picture include family member of dori without background.


## third problem:

### IRIS dataset from Sklearn

I use this dataset to solve an IRIS classification.
At first we shoud create train and test dataset.
then fit the algorithm with trainig data.

The Knn algorithm has a parameter which name is K.
I set K to 3,5,7,9,11.

and then use test data to evaluate the algorithm with different K. 

In the result part you can see the table of Accuracy for different K.


## fourth problem:

### Breast cancer dataset from Sklearn

I use this dataset to solve an Breast tumor classification.
At first we shoud create train and test dataset.
then fit the algorithm with trainig data.

The Knn algorithm has a parameter which name is K.
I set K to 3,5,7,9,11.

and then use test data to evaluate the algorithm with different K. 

In the result part you can see the table of Accuracy for different K.



## How to install
Run following command :

pip install -r requirements.txt


## How to Run

In each .ipynb file run each block to see the result. 

## Results

#### first problem:

nemo picture and mask and nemo picture after masking:(Trainig picture)



Input picture(a family member of nemo)


Output picture(a family member of nemo that detected and separated from background)




#### second problem:

dori picture and mask and dori picture after masking:(Trainig picture)



Input picture(a family member of dori)


Output picture(a family member of dori that detected and separated from background)




#### third problem:

result of accuracy for different K:

|               |   K=3    |           K=5          |            K=7          |           K=9           |           K=11          |
| ------------- | -------- | ---------------------- | ----------------------- | ----------------------- | ----------------------- |
| Accuracy      |     0.9  |    0.9666666666666667  |     0.9666666666666667  |     0.9666666666666667  |     0.9666666666666667  |

confusion matrice for three class:




#### Fourth problem:

result of accuracy for different K:

|               |           K=3           |           K=5          |            K=7          |           K=9           |           K=11          |
| ------------- | ----------------------- | ---------------------- | ----------------------- | ----------------------- | ----------------------- |
| Accuracy      |     0.9035087719298246  |    0.8947368421052632  |     0.8947368421052632  |     0.8947368421052632  |     0.8947368421052632  |

confusion matrice for two class:



