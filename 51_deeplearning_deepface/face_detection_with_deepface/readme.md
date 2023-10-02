# Hello Deep learning

In this session I use a deepface library for face recognition. 

Deepface is a library that use for extracting feature of human faces. 
This library used different deep learning algorithms for its purpose.

## Description

I've done some step to achieve end goal.

1. At first I write a function to use a dataset which include picture of different persons to produce features and labels.

   When all features are extracted, I stored them in ```input_data.csv``` file in dataset folder. I wrote a function which name is `generate_dataset` for this part. 

2. Then I preprocess data and onehot the labels. labels are the names of that persons that exist in the dataset.

3. And then I made a model with tensorflow to train the features with labels.

4. Finally I use sample pictures to predict person.

  My model can achieve 98% accuracy for train data and 82% accuracy for test data. Finally I stored my trained model in weights folder and named it ```face_model.h5``` .
 
 |           |       Loss     |        accuracy     |
 |---------: | :----------------: |:----------------: |
 |    Train            |       0.0117            |        0.9305          |
 |    Test            |        0.0340           |        0.8324           |
   

## How to install

```
pip install -r requirements.txt
```

##  How to run

1. Run Guys_dataset_colab.py file to generate dataset, onehot labels, train dataset and save it using below command in terminal:

```
python Guysdataset_colab.py
```

2. Run test_Model.py to use model that is created in last part and predict sample pictures with writing below command in terminal:

```
python test_model.py
```

