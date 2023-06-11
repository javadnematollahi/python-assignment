import arcade



class Heart(arcade.Sprite):
    def __init__(self,location):
        super().__init__("input/paddle.png")
        self.center_x=25+location*40
        self.center_y=18
        self.width=40
        self.height=10