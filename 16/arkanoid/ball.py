import random
import arcade

class Ball(arcade.Sprite):
    def __init__(self,game):
        super().__init__()
        self.center_x=game.width//2
        self.center_y=90
        self.radius=15
        self.width=self.radius*2
        self.height=self.radius*2
        self.color=arcade.color.YELLOW
        self.y=game.height
        self.x=game.width
        self.change_x=random.choice([-1,1])
        self.change_y=1
        self.speed=5

    def draw(self, *, filter=None, pixelated=None, blend_function=None):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.radius,self.color)
    def move(self):
        self.center_x+=self.change_x*self.speed
        self.center_y+=self.change_y*self.speed

        if self.center_x<0 or self.center_x>self.x:
            self.change_x*=-1
        if self.center_y>self.y:
            self.change_y*=-1