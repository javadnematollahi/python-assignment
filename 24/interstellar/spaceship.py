import arcade
from bullet import Bullet

class Spaceship(arcade.Sprite):
    def __init__(self,game,name):
        super().__init__(":resources:images/space_shooter/playerShip2_orange.png")
        #mokhtasat safine
        self.center_x=game.width/2
        self.center_y=50
        #arz o tol safine
        self.width=48
        self.height=48
        self.speed=8   # joze parametr hae arcade nist. khodeman tarif mikonim
        self.name=name
        self.change_x=0
        self.change_y=0
        self.game_width=game.width
        self.bullet_list=[]


   # def move(self,direction):
    def move(self):
     #   if direction=='L':
        if self.change_x==-1:
            if self.center_x> 0:
                self.center_x-=self.speed
     #   elif direction=='R':
        if self.change_x==1:
            if self.center_x< self.game_width:
               self.center_x+=self.speed

    def fire(self):
        new_bullet=Bullet(self)
        self.bullet_list.append(new_bullet)

    def bullet_rise_speed(self):
        Bullet(self).rise_speed()