#behtar ast ke aval ketabkhanehae khode python import shavad va 
#baad az on ketabkhanei ke ba pip nasb shode import shavad
# va baad az on ketabkhanehae ke khodeman neveshtim ra import mikpnim
#esme fileha bayad ba horofe kochik neveshte shavand
import random
import time
from typing import Optional
import arcade
from arcade import Texture
from spaceship import Spaceship
from enemy import Enemy
from heart import Heart

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1280,height=920,title="Interstellar")
        # arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background= arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.black_page=arcade.load_texture(".\\black.png")
# self dakhel parantez be property hae class Game eshare darad
# ba in kar mitavan be tamame property hae class game dastresi dasht        
        self.me=Spaceship(self,'javad')
        #self.enemy=Enemy(self)
        self.enemy_list=[]
        self.heart_list=[]
        self.collosion=0
        self.score=0
        self.laser = arcade.load_sound(':resources:sounds/laser2.wav',False)
        self.explosion = arcade.load_sound(':resources:sounds/explosion1.wav',False)
        self.gameover = arcade.load_sound(':resources:sounds/gameover3.wav',False)
        self.second=time.time()
        self.rise_speed=time.time()
        print(self.second)
        for i in range(3):
            heart_object=Heart(i)
            self.heart_list.append(heart_object)
        

    # in tabe baraye namayesh ast,yani chizhae ke gharar ast namayesh dade shavad
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)
        arcade.draw_text(str(self.score),self.width-60,15,arcade.color.WHITE,25,12)
        self.me.draw()
        #self.enemy.draw()
        for enemy in self.enemy_list:
            enemy.draw()
        for bullet in self.me.bullet_list:
            bullet.draw()
        for heart in self.heart_list:
            heart.draw()
        if len(self.heart_list)==0 or self.collosion==1:
            arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.black_page)
            arcade.draw_text("GAME OVER",self.width/3,self.height/2,arcade.color.ORANGE,36,15)
            # arcade.play_sound(self.gameover,1)

        arcade.finish_render() #baraye fahme bishtare barname neveshte mishavad,agar nanevisim ham moshkeli nist

    def on_key_press(self, symbol: int, modifiers: int):
        #symbol= code dokmehae keyboard ast  code A=97   code W=100
       # print(symbol)   symbol shomareye kilid ast
       # if symbol == 97:   #bere be chap   be jae inke code kilid(97) ra benevisim be sorate zir minevisim
        if symbol == arcade.key.LEFT or symbol==arcade.key.A:
           # self.me.move('L')
           self.me.change_x=-1
        elif symbol == arcade.key.RIGHT or symbol==arcade.key.D:   #bere be rast
           # self.me.move('R')
           self.me.change_x=1
        elif symbol == arcade.key.SPACE:
            self.me.fire()
            arcade.play_sound(self.laser,1)

    def on_key_release(self, symbol: int, modifiers: int):
        self.me.change_x=0
 

#tabei ke be sorat automatic tond tond ejra mishavad

#manteq bazi dakhel on_update neveshte mishavad
    def on_update(self, delta_time: float):

        if len(self.heart_list)!=0 and self.collosion==0:

            for enemy in self.enemy_list:
                if arcade.check_for_collision(enemy,self.me):
                    self.collosion=1
                    arcade.play_sound(self.gameover,1)
                    print("Game Over","\U0001F480")

            for enemy in self.enemy_list:
                if enemy.center_y<0:
                    self.enemy_list.remove(enemy)
                    self.heart_list.pop()
                    if len(self.heart_list)==0:
                        print("Game Over","\U0001F480")
                        arcade.play_sound(self.gameover,1)

            for bullet in self.me.bullet_list:
                if bullet.center_y > self.height:
                    self.me.bullet_list.remove(bullet)
                        
            for enemy in self.enemy_list:
                for bullet in self.me.bullet_list:
                    if arcade.check_for_collision(enemy,bullet):
                        self.enemy_list.remove(enemy)
                        self.me.bullet_list.remove(bullet)
                        arcade.play_sound(self.explosion,1)
                        self.score+=1

            self.me.move()

            for bullet in self.me.bullet_list:
                bullet.move()

            for enemy in self.enemy_list:
                enemy.move()
            # if random.randint(1,100)==6:
            
            if time.time()-self.second>=3:
                self.second=time.time()
                self.newenemy=Enemy(self)
                self.enemy_list.append(self.newenemy)

            if time.time()-self.rise_speed>=20:
                self.rise_speed=time.time()
                Enemy(self).rise_speed()
                self.me.bullet_rise_speed()

        else:
            self.enemy_list.clear()
            self.me.bullet_list.clear()
            self.me.kill()

window=Game()
arcade.run()