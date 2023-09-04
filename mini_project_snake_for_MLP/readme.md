# Snake with Machine learning algorithms

In this mini project I use MultiLayer Perceptron to train my snake in Snake game. 

History of snake game :

Snake first appeared on a Nokia device in 1997 on the Nokia 6110. It was adapted for Nokia devices by Taneli Armanto, a Design Engineer, User Interface Software.

## Description

I've done some step to achieve end goal.

1. At first I write a code for snake game with Arcade library. I've written this code in assignment 15 so I used that code in this mini project. 
   The snake of this game has one part in first and as you eat pears that appear in game, the part of the snake body is increased. This game need a human player to move the snake in game. player can use Right and Left and Up and Down key on keyboard to move the snake. 

   This version of snake game is written in main.py file.

2. Then I add a few lines of code to my first code to make the snake “smart”. In fact in this version of game the snake can move by itself and eat pears that appear in the game. The part of code that make my snake smart is Eatfood class that has a lot of conditions for snake moving. 
  These conditions include below rules:
  a. snake must move toward pears in the game.
  b. snake must be careful not to hit to right, left,top and down walls in the game.
  c. snake must be careful not to hit to part of its body.

  I also add a few lines of code to store some informations in a .csv file. 
  These informations include below features that I use them in my MLP algorithm in next step to train my model:
    
    |    Name of feature         |       description of feature     |
    | --- | --- |
    |    "last_up"               |  if last direction of snake moving is up, this parameter will be 1 otherwise will be 0  |
    |    "last_down"             |  if last direction of snake moving is down, this parameter will be 1 otherwise will be 0  |
    |    "last_right"            |  if last direction of snake moving is right, this parameter will be 1 otherwise will be 0  |
    |    "last_left"             |  if last direction of snake moving is left, this parameter will be 1 otherwise will be 0  |
    |    "food_up"               |  If the pear is on the top side of the snake, this parameter will be 1 otherwise will be 0 |
    |   "food_down"              |  If the pear is on the down side of the snake, this parameter will be 1 otherwise will be 0|
    |    "food_left"             |  If the pear is on the left side of the snake, this parameter will be 1 otherwise will be 0|
    |    "food_right"            |  If the pear is on the right side of the snake, this parameter will be 1 otherwise will be 0|
    |    "dist_x_to_body"        |  This parameter is the distance of snake head to part of its body if that part is on the top or down side of the snake head |
    |    "dist_y_to_body"        | This parameter is the distance of snake head to part of its body if that part is on the right or left side of the snake head |
    |    "dist_to_top_wall"      |  distance of snake head to top wall of game |
    |    "dist_to_down_wall"     |  distance of snake head to down wall of game |
    |    "dist_to_left_wall"     |  distance of snake head to left wall of game |
    |    "dist_to_right_wall"    |  distance of snake head to right wall of game |
    |    "Pear_center_x"         |  Location X of the center of the pear |
    |    "Pear_center_y"         |  Location Y of the center of the pear |
    |    "Pear_to_top"           | distance of pear to top wall of game |
    |    "Pear_to_bottom"        | distance of pear to bottom wall of game |
    |    "Pear_to_right"         | distance of pear to right wall of game |
    |    "Pear_to_left"          | distance of pear to left wall of game |

  Top features that I collected are inputs of MLP model. I must collect labels to able to train and test MLP model. 
  Labels that I collected are:

    |    Name of label         |       description of label     |
    | ------------------------ | ------------------------------ |
    |    "next_up"               |  if direction of snake moving is up, this parameter will be 1 otherwise will be 0  |
    |    "next_down"             |  if direction of snake moving is down, this parameter will be 1 otherwise will be 0  |
    |    "next_right"            |  if direction of snake moving is right, this parameter will be 1 otherwise will be 0  |
    |    "next_left"             |  if direction of snake moving is left, this parameter will be 1 otherwise will be 0  |

   Features are saved in input_data.csv file and Labels are saved in output_data.csv file. 

3. In this step I write a MLP model for my snake game that use some of top features and define the direction of snake moving. 

    I try different combination of top features for training model to define best features for training to get maximum accuracy and reduce the amount of calculations. As a result I removed below features from top features:

    "last_up", "last_down", "last_right",  "last_left"

   The specifications of my model are:

   * Model has three hidden layer and one input and one output layer
   * Neuron number of input layer: 16
   * Neuron number of first hidden layer: 80
   * Neuron number of second hidden layer: 64
   * Neuron number of third hidden layer: 48
   * Neuron number of output layer: 4
   * activation function of fisrt three layers:   relu
   * activation function of third hidden layer:   sigmoid
   * activation function of output layer:   softmax
   * optimizer:     AdamW
   * learning rate: 0.0001
   * loss function:   mean_squared_error
   * epochs number:      2000

  My MLP model can achieve 98% accuracy for train data and 96% accuracy for test data. Finally I save my trained model and named it "MLP_FOR_Snake.h5".
 

 loss and accuracy of train data:


 loss and accuracy of train and test data:

 4. In this step I copied my snake game code in a new .py file and make some changes in it. In fact I calculate features that I used them for training model and then I load my saved model which name was "MLP_FOR_Snake.h5" and I use the calculated features as inputs of model. The model use features and predict the direction moving of snake.

  You can see A view of the game in below:



    I should mentioned that if you run MLP_snake, each time you run, snake get different score. When I was testing it sometimes snake could get 80 to 90 score and sometimes snake could just get 10 score. But most of the time snake can get more than 30 scores.  

## How to install

pip install -r requirements.txt

##  How to run

### Collecting dataset :     main_ai.py  

you can type below command in terminal to run this file:    

python main_ai.py


### Create and training model:   trainmlp.ipynb

Run each part of this file to see the result.


### Use MLP for snake game:      MLP_snake.py

you can type below command in terminal to run this file:    

python MLP_snake.py

### play snake with keyborad keys     main.py




