## Tensoflow for expert

For training models we can use expert mode of tensorflow.
In this mode we have more access to layers and we can make some changes that we can't before.
I try expert mode of tensorflow on three dataset to test it.
1. mnist
2. cifar10
3. titanic


| Attempt | Test accurcy | Test loss | Train accuracy | Train loss |
| :-----: | :----------: | :-------: | :------------: | :--------: | 
| mnist | 0.97 | 0.075 | 0.99 | 0.008 | 
| cifar10 | 0.749 | 0.783 | 0.82 | 0.50 | 
| titanic | 0.77 | 0.491 | 0.81 | 0.407 | 