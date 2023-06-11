import arcade


class Brick(arcade.Sprite):
    def __init__(self,x,y,c,game):
        super().__init__()
        self.center_x=x
        self.center_y=y
        self.width=game.width//12
        self.height=30
        self.color=c

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)
        arcade.draw_rectangle_outline(self.center_x,self.center_y,self.width,self.height,arcade.color.BLACK,3)
