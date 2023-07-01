import arcade

class Heart(arcade.Sprite):
    def __init__(self,location ):
        super().__init__(".\heart.jpg")
        self.center_x=18+location*30
        self.center_y=18
        self.width=30
        self.height=30