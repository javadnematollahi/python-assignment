#behtar ast ke aval ketabkhanehae khode python import shavad va 
#baad az on ketabkhanei ke ba pip nasb shode import shavad
# va baad az on ketabkhanehae ke khodeman neveshtim ra import mikpnim
#esme fileha bayad ba horofe kochik neveshte shavand
import random
import arcade


class Spaceship(arcade.Sprite):
    def __init__(self,game):
        super().__init__(":resources:images/space_shooter/playerShip2_orange.png")
        #mokhtasat safine
        self.center_x=game.width/2
        self.center_y=50
        #arz o tol safine
        self.width=48
        self.height=48
        self.speed=8   # joze parametr hae arcade nist. khodeman tarif mikonim

class Enemy(arcade.Sprite):
    def __init__(self,game):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.center_x=random.randint(0,game.width)
        self.center_y=game.height+24
        self.width=48
        self.height=48
        self.angle=180
        self.speed=4


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=600,height=800,title="Interstellar")
        # arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background= arcade.load_texture(":resources:images/backgrounds/stars.png")
# self dakhel parantez be property hae class Game eshare darad
# ba in kar mitavan be tamame property hae class game dastresi dasht        
        self.me=Spaceship(self)
        self.doshman=Enemy(self)
   
    # in tabe baraye namayesh ast,yani chizhae ke gharar ast namayesh dade shavad
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)
        self.me.draw()
        self.doshman.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        #symbol= code dokmehae keyboard ast  code A=97   code W=100
        print(symbol)
        if symbol == 97:   #bere be chap
            self.me.center_x=self.me.center_x-self.me.speed
        elif symbol == 100:   #bere be rast
            self.me.center_x=self.me.center_x+self.me.speed

#tabei ke be sorat automatic tond tond ejra mishavad
    def on_update(self, delta_time: float):
        self.doshman.center_y-=self.doshman.speed



window=Game()
arcade.run()