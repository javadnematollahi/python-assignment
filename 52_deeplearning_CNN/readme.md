# Hello Deep learning

In this session I use four dataset from tensorflow to compare the result of MLP and CNN+MLP. I expect CNN+MLP has better results than MLP.

## Description

For each dataset I've made a MLP model and a CNN+MLP model. The results of two model for each dataset are shown in four below part.

These dataset's names are mnist, fashion mnist, cifar10 and cifar100. 


1. mnist

   This dataset is very simple and I can reach good result with a simple model MLP and  a CNN+MLP model.

|           |       Loss     |        accuracy     |
|---------: | :----------------: |:----------------: |
|    Train(MLP)            |       0.0298           |        0.9909           |
|    Test(MLP)            |        0.1015           |        0.9787           |
|    Train(CNN+MLP)            |       0.0119           |        0.9965           |
|    Test(CNN+MLP)            |        0.0434         |        0.9896           |  

2. fashion mnist

   This dataset is a little more complex than mnist dataset so I get weaker result rather than mnist dataset for both MLP and CNN+MLP.

|           |       Loss     |        accuracy     |
|---------: | :----------------: |:----------------: |
|    Train(MLP)            |       0.2654            |        0.9024           |
|    Test(MLP)            |        0.3435           |        0.8824          |
|    Train(CNN+MLP)            |       0.1420            |        0.9452           |
|    Test(CNN+MLP)            |        0.2688          |        0.9125           |  

3. cifar10

   This dataset is more complex than last two datasets and I get worse accuracy and loss result for both  both MLP and CNN+MLP.

|           |       Loss     |        accuracy     |
|---------: | :----------------: |:----------------: |
|    Train(MLP)            |       1.5054            |        0.4652           |
|    Test(MLP)            |        1.5106           |        0.4664           |
|    Train(CNN+MLP)            |       0.3275            |        0.8800           |
|    Test(CNN+MLP)            |        1.1673          |        0.7071           |

 4. cifar100 

   This dataset is the most complex of all and I get the worst accuracy and loss result.

|           |       Loss     |        accuracy     |
|---------: | :----------------: |:----------------: |
|    Train(MLP)            |       3.2879            |        0.2006           |
|    Test(MLP)            |        3.4148           |        0.1973           |
|    Train(CNN+MLP)           |       2.2498            |        0.4037           |
|    Test(CNN+MLP)           |        2.6611           |        0.3421           |
 
I compare the accuracy results of two models for four daasets in below table:

|                    |       MLP     |        CNN+MLP    |
|-------------------:| :-----------: |:----------------: |
|    Mnist           |   0.9787      |        0.9896     |
|    Fashion Mnist   |   0.882       |        0.9125     |
|    Cifar10         |    0.4664     |        0.7071     |
|    Cifar100        |    0.1973     |        0.3421     |

## How to install

```
pip install -r requirements.txt
```

##  How to run

1. To see the MLP result for mnist dataset run below command in terminal:

```
python MLP_for_mnist.py
```

To see the CNN+MLP result for mnist dataset run below command in terminal:

```
python CNN_MLP_for_mnist.py
```

2. To see the MLP result for fashion_mnist dataset run below command in terminal:

```
python MLP_for_fashion_mnist.py
```

To see the CNN+MLP result for fashion_mnist dataset run below command in terminal:

```
python CNN_MLP_for_fashion_mnist.py
```

3. To see the MLP result for cifar10 dataset run below command in terminal:

```
python MLP_for_cifar10.py
```

To see the CNN+MLP result for cifar10 dataset run below command in terminal:

```
python CNN_MLP_for_cifar10.py

4. To see the MLP result for cifar100 dataset run below command in terminal:

```
python MLP_for_cifar100.py
```

To see the CNN+MLP result for cifar100 dataset run below command in terminal:

```
python CNN_MLP_for_cifar100.py
```
