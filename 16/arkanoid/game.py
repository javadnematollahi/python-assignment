import arcade
import time
from rocket import Rocket
from start import Start
from brick import Brick
from heart import Heart
from ball import Ball
from rocket import Rocket

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=600,height=800,title="Arkanoid 2023")
        self.background_end= arcade.load_texture("input/background_end.jpg")
        self.background= arcade.load_texture("input/hexagon.png")
        self.start_page=arcade.load_texture("input/le.png")
        self.player=Rocket(self.width//2,60,"player",self)
        self.ball=Ball(self)
        self.bricks=[]
        self.heart=[]
        self.start=Start(self)
        self.show=1
        self.level=1
        self.endgame=0
        self.gameover=0
        self.heart_lenght=3
        self.delay=time.time()
        self.hit = arcade.load_sound(':resources:sounds/hit2.wav',False)
        self.hit1 = arcade.load_sound(':resources:sounds/hit3.wav',False)
        self.gameover1 = arcade.load_sound(':resources:sounds/gameover3.wav',False)
        self.lose = arcade.load_sound(':resources:sounds/lose2.wav',False)


    def on_draw(self):
        arcade.start_render()

        if self.level<5:
            if self.show==1:        
                arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.start_page)

                self.start.draw()
                if self.gameover==0:
                    arcade.draw_text(f"LEVEL {self.level}",self.width//2-90,self.height//2,arcade.color.WHITE,35)
                if self.gameover==1:
                    del self.ball
                    del self.player
                    del self.bricks
                    self.bricks=[]
                    self.player=Rocket(self.width//2,60,"player",self)
                    self.ball=Ball(self) 
                    self.heart_lenght=3
                    self.gameover=0
                    arcade.draw_text(5*" "+f"LEVEL {self.level}\n""START AGAIN",self.width//2-150,self.height//2+50,arcade.color.WHITE,35,multiline=True,width=500)
            elif self.show==2:
                arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)
                arcade.draw_text(f"LEVEL {self.level}"+55*" "+f"{self.player.score}",10,self.height-30,arcade.color.WHITE,20)
                self.player.draw()
                self.ball.draw()
                for heart in self.heart:
                    heart.draw()
                for brick in self.bricks:
                    brick.draw()
            elif self.show==3:    
                del self.ball
                # self.player=Rocket(self.width//2,60,"player",self)
                self.ball=Ball(self) 
                arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)
                arcade.draw_text(f"You Won LEVEL {self.level-1}\n\n"+4*" "+f"NEXT LEVEL\n"+6*" "+"Click Start",self.width//2-180,self.height//2+170,arcade.color.WHITE,35,multiline=True,width=600)
                self.start.draw()
        if self.level==5:
                arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background_end)
                arcade.draw_text(f"  Congragulation :)"+55*" "+f"You Won all levels",self.width//2-220,self.height-320,arcade.color.WHITE,40,multiline=True,width=600)
                       
        arcade.finish_render()

    def make_brick(self,level):
        colors=[arcade.color.GREEN,arcade.color.ORANGE,arcade.color.RED,
                arcade.color.GRAY,arcade.color.BLUE,arcade.color.CYAN,
                arcade.color.YELLOW,arcade.color.PURPLE,arcade.color.MAGENTA]
        for i in range(self.heart_lenght):
            heart_object=Heart(i)
            self.heart.append(heart_object)
        for j in range(3+level):
            for i in range(12):
                brick1=Brick((i*50)+25,self.height-100-(j*30),colors[j],self)
                self.bricks.append(brick1)

    def on_key_press(self, symbol: int, modifiers: int):
            if symbol==arcade.key.LEFT:
                self.player.change_x=-1
            elif symbol==arcade.key.RIGHT:
                self.player.change_x=1
    
    def on_key_release(self, symbol: int, modifiers: int):
        if symbol==arcade.key.LEFT or symbol==arcade.key.RIGHT:
            self.player.change_x=0

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if self.start.center_x-self.start.width//2<x<self.start.center_x+self.start.width//2 and\
        self.start.center_y-84-self.start.height//2<y<self.start.center_y-84+self.start.height//2 and\
        button==arcade.MOUSE_BUTTON_LEFT:
            if self.show==1:
                self.show=2
                
            elif self.show==3:
                self.show=2
            del self.start
            self.make_brick(self.level)
        
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.player.width//2<x<self.width-self.player.width//2:
            self.player.center_x=x

    def on_update(self, delta_time: float):
        if self.show==2 and self.gameover==0:
            if arcade.check_for_collision(self.player,self.ball):
                
                if time.time()-self.delay>0.1:
                    self.delay=time.time()
                    self.ball.change_y*=-1
                
                arcade.play_sound(self.hit1,1)
            self.player.move()
            self.ball.move()

            if self.ball.center_y<self.player.center_y:
                del self.ball
                self.ball=Ball(self)
                self.heart.pop()
                for heart in self.heart:
                    heart.draw()
                self.heart_lenght-=1
                if self.heart_lenght!=0:
                    arcade.play_sound(self.lose,1)
                if self.heart_lenght==0:
                    self.level=1
                    self.gameover=1
                    self.start=Start(self)
                    self.show=1
                    arcade.play_sound(self.gameover1,1)
                    

            for i in self.bricks:
                if arcade.check_for_collision(i,self.ball):
                    if i.center_y-i.height//2-7 < self.ball.center_y<i.center_y+i.height//2+7:
                        self.ball.change_x*=-1
                    else:
                        self.ball.change_y*=-1
                    self.bricks.remove(i)
                    arcade.play_sound(self.hit,1)
                    self.player.score+=1
                    if len(self.bricks)==0:
                        self.level+=1
                        self.ball.speed+=1
                        if self.level==5:
                            self.endgame=1
                        self.start=Start(self)
                        self.show=3