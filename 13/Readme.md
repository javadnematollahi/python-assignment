#13

There is two python file in 13.
The first file which name is complexloop_box.py used for drawing a picture similar to below picture.


![complexloop_box](https://user-images.githubusercontent.com/86910174/234556094-55178c54-1b82-4337-9a74-5b1831d0fc00.jpg)


As you can see in complexloop_box.py, you should use arcade library. 
Drawing 100 rhombus could be done by using a for loop nested inside another for loop. each for loop count from 0 to 10 and in each step, a rhombus is created in plane.
Another point is about creating rhombus. to make this happen use a function which creates triangle, then draw Two triangles whose bases are joined together.
further more you should change the color of rhombus between red and blue. To do this you can use two 'if' that define color.

The Second file is 'interstellar.py' which is a game about a spaceship in space that want to fight another spaceship.

in this code arcade library is also used. three class in this file is made whose names are Spaceship,Enemy,Game.
The Spaceship class define the property of our spaceship which include shape, size,location and speed.
The Enemy class define the property of enemy spaceship which include shape, size,location and speed.
The Game class define the enviroment properties of game which include size of window, background image and title of the game. three functions are defined in this class.
the first function is on_draw. this function help us to show whatever you can see in the game like spaceships, window of game, background image.
the second function is on_key_press. this function help us to move our spaceship in two direction toward left and right.
the third function is on_update. this function is called over and over again and we use it to move enemy spaceship from top to down of the game window.

The enviroment of game is shown below.

![interstellar](https://user-images.githubusercontent.com/86910174/234574100-b2807d97-ff5a-4fa0-a390-36dd102618a8.jpg)
