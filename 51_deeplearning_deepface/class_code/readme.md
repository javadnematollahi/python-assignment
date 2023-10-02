# Hello Deep learning

In this session I use three dataset from tensorflow to explain why we need to use deep learning algorithm. 

## Description

I've trained mnist, fashion mnist, cifar10 datasets that exist in tensorflow website. In these three dataset, first of all I flat each picture and
use the value of pixels as input of MLP.

1. mnist

   This dataset is very simple and I can reach good result with a simple MLP in 5 epochs.

|           |       Loss     |        accuracy     |
|---------: | :----------------: |:----------------: |
|    Train            |       0.0765            |        0.9755          |
|    Test            |        0.0723           |        0.9786           |   

2. fashion mnist

   This dataset is a little more complex than mnist dataset so I get weaker result rather than mnist dataset.

|           |       Loss     |        accuracy     |
|---------: | :----------------: |:----------------: |
|    Train            |       0.3545            |        0.8712           |
|    Test            |        0.3545           |       0.8712           |   

3. cifar10

   This dataset is the most complex of all and I get bad accuracy and loss result, eventhough I use more complex MLP rather than last two dataset.

|           |       Loss     |        accuracy     |
|---------: | :----------------: |:----------------: |
|    Train            |       1.5168            |        0.4574           |
|    Test            |        1.5168           |        0.45739           |   

 
When we compare the results, we know that as the data become more complex, we have less chance to use MLP for solving our problem and we should use deep learning algorithm.   

## How to install

```
pip install -r requirements.txt
```

##  How to run

1. To see the result for mnist dataset run below command in terminal:

```
python MLP_for_mnist.py
```
2. To see the result for fashion_mnist dataset run below command in terminal:

```
python MLP_for_fashion_mnist.py
```

3. To see the result for cifar10 dataset run below command in terminal:

```
python MLP_for_cifar10.py
```
