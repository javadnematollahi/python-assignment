import arcade


class Rocket(arcade.Sprite):
    def __init__(self,x,y,n,game):
        super().__init__("input/paddle.png")

        self.center_x=x
        self.center_y=y
        self.name=n
        self.change_x=0
        self.change_y=0
        self.width=130
        self.height=20
        self.speed=4
        self.score=0
        self.x=game.width

    def move(self):
        self.center_x+=self.change_x*self.speed

        if self.width//2>self.center_x:
            self.center_x=self.width//2
        if self.center_x>self.x-self.width//2:
            self.center_x=self.x-self.width//2