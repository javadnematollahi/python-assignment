import time
import arcade

class Start(arcade.Sprite):
    def __init__(self,game):
        super().__init__()
        self.starts=arcade.load_texture("input/play.jpg")
        self.center_x=game.width//2
        self.center_y=game.height//2
        self.width=200
        self.height=70
        self.second=0
        self.color=arcade.color.GREEN

    def draw(self):
        arcade.draw_lrwh_rectangle_textured(self.center_x//2+50,self.center_y//2+80,self.width,self.height,self.starts)
        arcade.draw_rectangle_outline(self.center_x,self.center_y-84,self.width,self.height,self.color,7)
        if time.time()-self.second>0.5:
            self.second=time.time()
            if int(self.second)%2==1:
                self.color=arcade.color.WHITE
            elif int(self.second)%2==0:
                self.color=arcade.color.GREEN