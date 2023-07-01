import random
import arcade


class Enemy(arcade.Sprite):
    speed=2
    def __init__(self,game):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.center_x=random.randint(0,game.width)
        self.center_y=game.height+24
        self.width=48
        self.height=48
        self.angle=180
        # self.speed=2
        

    def move(self):
        self.center_y-= Enemy.speed

    def rise_speed(self):
        Enemy.speed+=1
        print(Enemy.speed)