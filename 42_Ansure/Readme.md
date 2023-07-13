
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

![stature](https://github.com/javad7189/python-assignment/assets/86910174/c8362bcd-f5d2-46a4-ae9c-a0b9df3c8422)



The shouldercircumference of women and men:
this feature is good for classifying men and women.


![shouldercircumference](https://github.com/javad7189/python-assignment/assets/86910174/2eca6849-eaa6-4dd6-809c-24571c0ce5b3)


Below code is used for splitting data to train and test:

![split](https://github.com/javad7189/python-assignment/assets/86910174/c3dba0da-037f-4e7a-bb9c-be15bb49a3cc)


Accuray for my knn algorithm for some K:

![accuracymyknn](https://github.com/javad7189/python-assignment/assets/86910174/174f0057-f918-4311-a8c1-738c0ba14ad9)


Confusion matrix for myknn algorithm:

![confusionmyknn](https://github.com/javad7189/python-assignment/assets/86910174/d6701d35-cb0e-438e-97f0-6c8ccfb9734b)


Accuracy for two algorithm: Myknn and sklearn


![twoknn](https://github.com/javad7189/python-assignment/assets/86910174/9e90f5ed-bedc-487d-886f-eff2e4adb4fa)


Confusion matrix for sklearn algorithm:

![sklearnknn](https://github.com/javad7189/python-assignment/assets/86910174/cbb79983-2212-4268-a5d6-466d6768533f)







