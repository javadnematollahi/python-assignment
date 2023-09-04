import arcade
import tensorflow as tf
import numpy as np
from apple import *
from snake import Snake





class Eatfood():
    def __init__(self,game):
        self.game_class=game
        self.direction=0
        self.apple=1
        self.pear=0
        self.immediate_change_up=0
        self.immediate_change_down=0
        self.immediate_change_left=0
        self.immediate_change_right=0
        self.save=0
        self.up=0
        self.down=0
        self.right=0
        self.left=0
        self.last_out=6


    def eat_pear(self):

        self.dist_x_to_body=0
        self.dist_y_to_body=0
        if self.game_class.snake.change_y==1:
            self.up=1
        if self.game_class.snake.change_y==-1:
            self.down=1
        if self.game_class.snake.change_x==1:
            self.right=1
        if self.game_class.snake.change_x==-1:
            self.left=1



        if self.game_class.snake.change_y==1:    
            for i,part in enumerate(self.game_class.snake.body):
                if part['y']-64<self.game_class.snake.center_y<part['y'] and self.game_class.snake.center_x==part['x']:
                    self.dist_x_to_body=self.game_class.snake.center_x-part['x']
                    self.dist_y_to_body=self.game_class.snake.center_y-part['y']
        if self.game_class.snake.change_y==-1:    
            for i,part in enumerate(self.game_class.snake.body):
                if part['y']<self.game_class.snake.center_y<part['y']+64 and self.game_class.snake.center_x==part['x']:
                    self.dist_x_to_body=self.game_class.snake.center_x-part['x']
                    self.dist_y_to_body=self.game_class.snake.center_y-part['y']
        if self.game_class.snake.change_x==1:    
            for i,part in enumerate(self.game_class.snake.body):
                if part['x']-64<self.game_class.snake.center_x<part['x'] and self.game_class.snake.center_y==part['y']:
                    self.dist_x_to_body=self.game_class.snake.center_x-part['x']
                    self.dist_y_to_body=self.game_class.snake.center_y-part['y']
        if self.game_class.snake.change_x==-1:    
            for i,part in enumerate(self.game_class.snake.body):
                if part['x']<self.game_class.snake.center_x<part['x']+64 and self.game_class.snake.center_y==part['y']:
                    self.dist_x_to_body=self.game_class.snake.center_x-part['x']
                    self.dist_y_to_body=self.game_class.snake.center_y-part['y']


        self.food_right=0 ; self.food_left=0 ; self.food_up=0 ; self.food_down=0 
        
        if (self.game_class.pear.center_x-self.game_class.snake.center_x)>0:
            self.food_right=1
        elif (self.game_class.pear.center_x-self.game_class.snake.center_x)<0:
            self.food_left=1
        elif (self.game_class.pear.center_y-self.game_class.snake.center_y)>0:
            self.food_up=1
        elif (self.game_class.pear.center_y-self.game_class.snake.center_y)<0:
            self.food_down=1        

        # out=self.game_class.model.predict([[self.up,self.down,self.right,self.left,
        out=self.game_class.model.predict([[
            self.food_up,self.food_down,self.food_left,self.food_right,
            self.dist_x_to_body,self.dist_y_to_body,
            800-self.game_class.snake.center_y,
            self.game_class.snake.center_y,
            self.game_class.snake.center_x,
            800-self.game_class.snake.center_x,
            self.game_class.pear.center_x,self.game_class.pear.center_y,
            800-self.game_class.pear.center_y,self.game_class.pear.center_y,800-self.game_class.pear.center_x,self.game_class.pear.center_x]])
        out=np.argmax(out)


        print(f"out: {out}     last_out: {self.last_out}")
        if out  ==0 and self.last_out!=1:
            self.game_class.snake.change_y=1
            self.game_class.snake.change_x=0
            self.last_out=0
        elif out  ==1 and self.last_out!=0:
            self.game_class.snake.change_y=-1
            self.game_class.snake.change_x=0
            self.last_out=1
        elif out  ==2 and self.last_out!=3:
            self.game_class.snake.change_x=1
            self.game_class.snake.change_y=0
            self.last_out=2
        elif out ==3 and self.last_out!=2:
            self.game_class.snake.change_x=-1
            self.game_class.snake.change_y=0
            self.last_out=3

        
    def eat_apple(self):

            if self.direction==0:
                if self.game_class.snake.change_y==0:
                    if self.game_class.snake.center_x>=776  or self.game_class.snake.center_x<=24:
                        self.direction=2
                if self.game_class.apple.center_x>self.game_class.snake.center_x:
                        if self.game_class.snake.change_x!=-1:
                            self.game_class.snake.change_y=0
                            self.game_class.snake.change_x=1
                            print('right')
                elif self.game_class.apple.center_x<self.game_class.snake.center_x:
                        if self.game_class.snake.change_x!=1:
                            self.game_class.snake.change_y=0
                            self.game_class.snake.change_x=-1
                            print('left')

            if self.direction==2:
                if self.game_class.snake.change_x==0:
                    if self.game_class.snake.center_y>=784  or self.game_class.snake.center_y<=16:
                        self.direction=0
                if self.game_class.apple.center_y>self.game_class.snake.center_y:
                        if self.game_class.snake.change_y!=-1:
                            self.game_class.snake.change_x=0
                            self.game_class.snake.change_y=1
                            print('up')
                elif self.game_class.apple.center_y<self.game_class.snake.center_y:
                        if self.game_class.snake.change_y!=1:
                            self.game_class.snake.change_x=0
                            self.game_class.snake.change_y=-1  
                            print('down')
            if self.game_class.snake.change_x!=0:
                if self.game_class.apple.center_x-16<=self.game_class.snake.center_x and self.game_class.snake.center_x<=self.game_class.apple.center_x+16:
                        self.direction=2
            if self.game_class.snake.change_y!=0:
                if self.game_class.apple.center_y-16<=self.game_class.snake.center_y and self.game_class.snake.center_y<=self.game_class.apple.center_y+16:
                        self.direction=0


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=800, title="Super Snake V1")
        self.apple=Apple(self)
        self.pear=Pear(self)
        self.poo=Poo(self)
        self.snake=Snake(self)
        self.eat=Eatfood(self)
        self.model= tf.keras.models.load_model("MLP_FOR_Snake.h5")

        self.gameover_outfit=0
        self.gameover_collision=0
        self.gameoverzero=0
        arcade.set_background_color(arcade.color.KHAKI)
        


    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(self.snake.score,self.width-60,10,arcade.color.GRAY,28,16)

        if self.gameoverzero==0 and self.gameover_outfit==0 and self.gameover_collision==0:
            self.poo.draw()
            self.pear.draw()
            
        if self.gameoverzero==1 or self.gameover_outfit==1 or self.gameover_collision==1:
            self.snake.change_x=0
            self.snake.change_y=0
            arcade.draw_text('GAME OVER',self.width//4,self.height//2,arcade.color.RED,28,16)
            arcade.draw_text(f'Your score:{self.snake.score}',135,200,arcade.color.RED,28,16)
        self.gameover_collision=self.snake.draw()
        arcade.finish_render()

    


    def on_update(self, delta_time):

            self.eat.eat_pear()
            if self.gameover_collision==0 and self.gameover_outfit==0 and self.gameoverzero==0:
                self.gameover_outfit=self.snake.move()

            if arcade.check_for_collision(self.snake,self.pear):   
                self.gameoverzero=self.snake.eat(self.pear,2)   
                self.pear=Pear(self)
            if arcade.check_for_collision(self.snake,self.poo):
                self.gameoverzero=self.snake.eat(self.poo,3) 
                self.poo=Poo(self)


    

if __name__ == "__main__":
    
    game=Game()
    arcade.run()
    

