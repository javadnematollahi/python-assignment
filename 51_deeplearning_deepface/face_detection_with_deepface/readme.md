# Hello Deep learning

In this session I use a deepface library for face recognition. 

Deepface is a library that use for extracting feature of human faces. 
This library used different deep learning algorithms for its purpose.

## Description

I've done some step to achieve end goal.

1. At first I write a function to use a dataset which include picture of different persons to produce features and labels.

   When all features are extracted, I stored them in ```input_data.csv``` file in dataset folder.

2. Then I preprocess data and onehot the labels. labels are the names of that persons that exist in the dataset.

3. And then I made a model with tensorflow to train the features with labels.

4. Finally I use sample pictures to predict person.

  My model can achieve 98% accuracy for train data and 82% accuracy for test data. Finally I stored my trained model in weights folder and named it ```face_model.h5``` .
 
 |           |       Loss     |        accuracy     |
 |---------: | :----------------: |:----------------: |
 |    Train            |       0.0012            |        0.9981           |
 |    Test            |        0.0524           |        0.8208           |
 
I made two file, one for use in google colab and other for using in local system. Both of these files do same work and you can use one of them base on system you run code on it.

Use ```Guys_dataset_colab.ipynb``` file in google colab.

Use ```Guys_dataset_local.ipynb``` file in system.    

## How to install

```
pip install -r requirements.txt
```

##  How to run

Run each cell from top to bottom.

