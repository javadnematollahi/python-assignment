
# Machine learning 5_ Ansure

In this section we solve a classification problem to classify ansure database.

The algorithm that we use is KNN that we write and Knn from scikit library.
I use this algorithm for two classes which include women and men.

The Knn algorithm has a parameter which name is K.
I set K to 3,5,7,9,11.




The feature that we use is shouldercircumference. I train the KNN algorithm with shouldercircumference of women and men.

## How to install
Run following command :

pip install -r requirements.txt


## How to Run

In each .ipynb file run each block to see the result. 

## Results

The stature of women and men:




The shouldercircumference of women and men:
this feature is good for classifying men and women.




Below code is used for splitting data to train and test:



Accuray for my knn algorithm for some K:


Confusion matrix for myknn algorithm:


Accuracy for two algorithm: Myknn and sklearn




Confusion matrix for sklearn algorithm:








