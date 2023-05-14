import random
import arcade
from main import Game

class Fruit(arcade.Sprite):
    def __init__(self,game,name):
        super().__init__(name)
        self.width=32
        self.height=32
        self.center_x=random.randint(10,game.width-10)
        self.center_y=random.randint(10,game.height-10)
        self.change_x=0
        self.change_y=0

class Poo(Fruit):
    def __init__(self, game):
        super().__init__(game,'poo.png')

class Pear(Fruit):
    def __init__(self, game):
        super().__init__(game,'pear.png')


class Apple(Fruit):
    def __init__(self, game):
        super().__init__(game,'apple.png')