
# Sudoku
In these project I write a code for sudoku.

sudoku is a game with below rules:

1. You just use these numbers in sudoku
    [1,2,3,4,5,6,7,8,9]
2. In each row you should put one of 1 to 9 number and you cant set a number in two cell in a row. 
   if you do this, the game will change the background color of that cell to red.
3. In each column you should put one of 1 to 9 number and you cant set a number in two cell in a
   column. if you do this, the game will change the background color of that cell to red.
4. In each square you should put one of 1 to 9 number and you cant set a number in two cell in a 
   square. if you do this, the game will change the background color of that cell to red.
5. If you find the number of all empty cells, you will win the game.


This game has below features:

1. there is a menu which name is Game. there are 7 item in menu that you can choose one of them. Iexplain all of the from top to 
   bottom respectvily:

   a: Back to game: when you move to ther pages and you want to back to game to continue your game, you must use this item.
   b: New: when you solve all empty cell and you win or you dont like to continue a game, you can choose new from menu to start  a new game.
   c: Open file: when you want to import your sudoku numbers to play  and solve it, you must choose
      this item and then chose your .txt file.
   d: solve current game: If you can't find a solution for the current game you can choose this to allow the game to solve the game by itself.
   e: About: by choosing this item you can read some information about sudoku. 
   f: Help: by choosing this item you can read the rules of sudoku.
   g: Exit: by choosing this item you can close the game.
2. there is switch or toggle bottun in the left-top of game window that you can change the urrent mode to dark mode by toggle it.
3. when you write a number in a cell so that there is another number equal your number in the row of that number or in the 
   column of that number or in the square of that number, background color of that cell will be change o red. and if you
   change that number to a number that there isnt another equal number in row and column and square of that cell,
   then the color of that cell will back to white.
4. if you can find all numbers, then yu wil win and a box with below message will be shown to you:
                  "congratulation!"
5. If you import an invalid text file as input, a box with message below will be shown to you:
                  "puzzle is invalid"




I use pyinstaller library for this project to make an exe file so that you can download only the my_sudoku.exe to run the sudoku software.



## How to install

Run following command :

pip install -r requirements.txt


## How to Run
execute this command in terminal:
python my_sudoku.py


## Results

different pages of game are shown below:

main page:

![first](https://github.com/javad7189/python-assignment/assets/86910174/bb2285cc-bc9c-4886-9b61-b3e9513e915b)


win page:

![winpage](https://github.com/javad7189/python-assignment/assets/86910174/5f0fb0c7-9d26-477c-97d3-011c4dbaf41f)



About page:

![about](https://github.com/javad7189/python-assignment/assets/86910174/9396c364-2adb-4784-a0d1-927336df3a59)



Help page:

![help](https://github.com/javad7189/python-assignment/assets/86910174/752f0a01-dd22-4ca8-8443-0714de773c0e)














