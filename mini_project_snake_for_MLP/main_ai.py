import arcade
import pandas as pd
from apple import *
from snake import Snake
import time
import csv,os

class data():
    def __init__(self):
        self.last_up=0
        self.last_down=0
        self.last_left=0
        self.last_right=0
        self.dist_x_to_food=0
        self.food_up=0
        self.food_down=0
        self.food_right=0
        self.food_left=0
        self.dist_y_to_food=0
        self.dist_x_to_body=0
        self.dist_y_to_body=0
        self.dist_to_top_wall=0
        self.dist_to_down_wall=0
        self.dist_to_left_wall=0
        self.dist_to_right_wall=0
        self.next_up=0
        self.next_down=0
        self.next_left=0
        self.next_right=0
        self.list_input=[]
        self.list_output=[]


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
        self.data=data()
        self.save=0

    def eat_pear(self):
        self.data.last_up=0;self.data.last_down=0; self.data.last_left=0; self.data.last_right=0       
        if self.game_class.snake.change_y==1:
            self.data.last_up=1
        elif self.game_class.snake.change_y==-1:
            self.data.last_down=1
        if self.game_class.snake.change_x==1:
            self.data.last_right=1
        elif self.game_class.snake.change_x==-1:
            self.data.last_left=1

        self.data.dist_x_to_body=0
        self.data.dist_y_to_body=0
        if self.direction==0:
            # if self.game_class.snake.change_y==0:
            if self.game_class.snake.center_x>=784  or self.game_class.snake.center_x<=16:
                print("XXX_axis_out")
                self.direction=2
                self.save=0
            if self.game_class.pear.center_x>self.game_class.snake.center_x:
                for i,part in enumerate(self.game_class.snake.body):
                    if part['x']-96<self.game_class.snake.center_x<part['x'] and self.game_class.snake.center_y==part['y']:
                        self.data.dist_x_to_body=self.game_class.snake.center_x-part['x']
                        self.data.dist_y_to_body=self.game_class.snake.center_y-part['y']
                        break
                else:
                    if self.game_class.snake.change_x!=-1:
                        self.game_class.snake.change_y=0
                        self.game_class.snake.change_x=1
                        print(f'right    {self.direction}')
            elif self.game_class.pear.center_x<self.game_class.snake.center_x:
                for i,part in enumerate(self.game_class.snake.body):
                    if part['x']<self.game_class.snake.center_x<part['x']+96 and self.game_class.snake.center_y==part['y']:
                        self.data.dist_x_to_body=self.game_class.snake.center_x-part['x']
                        self.data.dist_y_to_body=self.game_class.snake.center_y-part['y']
                        break
                else:
                    if self.game_class.snake.change_x!=1:
                        self.game_class.snake.change_y=0
                        self.game_class.snake.change_x=-1
                        print(f'left    {self.direction}')
            if self.immediate_change_up==1 or self.immediate_change_down==1:
                left_i=0
                right_i=0
                for i,part in enumerate(self.game_class.snake.body):
                    if self.game_class.snake.center_x<part['x'] and self.game_class.snake.center_y==part['y']:
                        right_i=i
                    if self.game_class.snake.center_x>part['x'] and self.game_class.snake.center_y==part['y']:
                        left_i=i
                if left_i<right_i:
                    if self.game_class.snake.change_x!=1:
                        self.game_class.snake.change_y=0
                        self.game_class.snake.change_x=-1
                        self.data.dist_x_to_body=self.game_class.snake.center_x-part['x']
                        self.data.dist_y_to_body=self.game_class.snake.center_y-part['y']
                        print(f'left    {self.direction}')
                elif left_i>right_i:
                    if self.game_class.snake.change_x!=-1:
                        self.game_class.snake.change_y=0
                        self.game_class.snake.change_x=1
                        self.data.dist_x_to_body=self.game_class.snake.center_x-part['x']
                        self.data.dist_y_to_body=self.game_class.snake.center_y-part['y']
                        print(f'right    {self.direction}')
                self.immediate_change_up=0
                self.immediate_change_down=0


        if self.direction==2:
            # if self.game_class.snake.change_x==0:
            if self.game_class.snake.center_y>=784  or self.game_class.snake.center_y<=16:
                print("YYY_axis_out")
                self.direction=0
                self.save=0
            if self.game_class.pear.center_y>self.game_class.snake.center_y:
                for i,part in enumerate(self.game_class.snake.body):
                    if part['y']-96<self.game_class.snake.center_y<part['y'] and self.game_class.snake.center_x==part['x']:
                        self.data.dist_x_to_body=self.game_class.snake.center_x-part['x']
                        self.data.dist_y_to_body=self.game_class.snake.center_y-part['y']
                        break
                else:
                    if self.game_class.snake.change_y!=-1:
                        self.game_class.snake.change_x=0
                        self.game_class.snake.change_y=1
                        print(f'up    {self.direction}')
            elif self.game_class.pear.center_y<self.game_class.snake.center_y:
                for i,part in enumerate(self.game_class.snake.body):
                    if part['y']<self.game_class.snake.center_y<part['y']+96 and self.game_class.snake.center_x==part['x']:
                        self.data.dist_x_to_body=self.game_class.snake.center_x-part['x']
                        self.data.dist_y_to_body=self.game_class.snake.center_y-part['y']
                        break
                else:
                    if self.game_class.snake.change_y!=1:
                        self.game_class.snake.change_x=0
                        self.game_class.snake.change_y=-1  
                        print(f'down    {self.direction}')
            if self.immediate_change_right==1 or self.immediate_change_left==1:
                up_i=0
                down_i=0
                for i,part in enumerate(self.game_class.snake.body):
                    if self.game_class.snake.center_y<part['y'] and self.game_class.snake.center_x==part['x']:
                        up_i=i
                    if self.game_class.snake.center_y>part['y'] and self.game_class.snake.center_x==part['x']:
                        down_i=i
                if up_i<down_i:
                    if self.game_class.snake.change_y!=-1:
                        self.game_class.snake.change_x=0
                        self.game_class.snake.change_y=1
                        self.data.dist_x_to_body=self.game_class.snake.center_x-part['x']
                        self.data.dist_y_to_body=self.game_class.snake.center_y-part['y']
                        print(f'up    {self.direction}')
                elif up_i>down_i:
                    if self.game_class.snake.change_y!=1:
                        self.game_class.snake.change_x=0
                        self.game_class.snake.change_y=-1
                        self.data.dist_x_to_body=self.game_class.snake.center_x-part['x']
                        self.data.dist_y_to_body=self.game_class.snake.center_y-part['y']
                        print(f'down    {self.direction}')
                self.immediate_change_right=0
                self.immediate_change_left=0

                
        self.data.next_up=0;self.data.next_down=0; self.data.next_left=0; self.data.next_right=0       
        if self.game_class.snake.change_y==1:
            self.data.next_up=1
        elif self.game_class.snake.change_y==-1:
            self.data.next_down=1
        if self.game_class.snake.change_x==1:
            self.data.next_right=1
        elif self.game_class.snake.change_x==-1:
            self.data.next_left=1
        self.data.dist_to_top_wall=800-self.game_class.snake.center_y
        self.data.dist_to_down_wall=self.game_class.snake.center_y
        self.data.dist_to_left_wall=self.game_class.snake.center_x
        self.data.dist_to_right_wall=800-self.game_class.snake.center_x
        self.data.dist_x_to_food=self.game_class.pear.center_x-self.game_class.snake.center_x
        self.data.dist_y_to_food=self.game_class.pear.center_y-self.game_class.snake.center_y


        self.data.food_right=0 ; self.data.food_left=0 ; self.data.food_up=0 ; self.data.food_down=0 
        
        if self.data.dist_x_to_food>0:
            self.data.food_right=1
        elif self.data.dist_x_to_food<0:
            self.data.food_left=1
        elif self.data.dist_y_to_food>0:
            self.data.food_up=1
        elif self.data.dist_y_to_food<0:
            self.data.food_down=1            

        self.data.list_input.append({"last_up":self.data.last_up, "last_down":self.data.last_down,"last_right":self.data.last_right, "last_left":self.data.last_left, "food_up":self.data.food_up,
                        "food_down":self.data.food_down,"food_left":self.data.food_left,"food_right":self.data.food_right,"dist_x_to_body":self.data.dist_x_to_body,
                        "dist_y_to_body":self.data.dist_y_to_body,"dist_to_top_wall":self.data.dist_to_top_wall,"dist_to_down_wall":self.data.dist_to_down_wall, "dist_to_left_wall":self.data.dist_to_left_wall,
                        "dist_to_right_wall":self.data.dist_to_right_wall,"Pear_center_x":self.game_class.pear.center_x,"Pear_center_y":self.game_class.pear.center_y
                        ,"Pear_to_top":800-self.game_class.pear.center_y,"Pear_to_bottom":self.game_class.pear.center_y
                        ,"Pear_to_right":800-self.game_class.pear.center_x,"Pear_to_left":self.game_class.pear.center_x})

        self.data.list_output.append({"next_up":self.data.next_up, "next_down":self.data.next_down,"next_right":self.data.next_right, "next_left":self.data.next_left})



        if self.game_class.snake.change_x!=0:
            if self.save==0:
                if self.game_class.pear.center_x-16<=self.game_class.snake.center_x and self.game_class.snake.change_x==1 or self.game_class.snake.center_x<=self.game_class.pear.center_x+16 and self.game_class.snake.change_x==-1:
                        self.direction=2
            for i,part in enumerate(self.game_class.snake.body):
                if self.game_class.snake.center_y==part['y'] and part['x']-128<self.game_class.snake.center_x<part['x'] and self.game_class.snake.change_x==1:
                     self.direction=2
                     self.immediate_change_right=1
                     print('immediate_change_right')
                     self.save=1
                if self.game_class.snake.center_y==part['y'] and (part['x'])<self.game_class.snake.center_x<(part['x']+128) and self.game_class.snake.change_x==-1:
                     self.direction=2
                     self.immediate_change_left=1
                     print('immediate_change_left')
                     self.save=1
        if self.game_class.snake.change_y!=0:
            if self.save==0:
                if self.game_class.pear.center_y-16<=self.game_class.snake.center_y and self.game_class.snake.change_y==1 or self.game_class.snake.center_y<=self.game_class.pear.center_y+16 and self.game_class.snake.change_y==-1:
                        self.direction=0
            for i,part in enumerate(self.game_class.snake.body):
                if self.game_class.snake.center_x==part['x'] and part['y']-128<self.game_class.snake.center_y<part['y'] and self.game_class.snake.change_y==1:
                     self.direction=0
                     self.immediate_change_up=1
                     print('immediate_change_up')
                     self.save=1
                if self.game_class.snake.center_x==part['x'] and (part['y'])<self.game_class.snake.center_y<(part['y']+128) and self.game_class.snake.change_y==-1:
                     self.direction=0
                     self.immediate_change_down=1
                     print('immediate_change_down')
                     self.save=1


        
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
                    if self.game_class.snake.center_y>=776  or self.game_class.snake.center_y<=24:
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
                if self.game_class.apple.center_x-16<self.game_class.snake.center_x and self.game_class.snake.center_x<self.game_class.apple.center_x+16:
                        self.direction=2
            if self.game_class.snake.change_y!=0:
                if self.game_class.apple.center_y-16<self.game_class.snake.center_y and self.game_class.snake.center_y<self.game_class.apple.center_y+16:
                        self.direction=0


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=800, title="Super Snake V1")
        self.apple=Apple(self)
        self.pear=Pear(self)
        self.poo=Poo(self)
        self.snake=Snake(self)
        self.eat=Eatfood(self)
        self.gameover_outfit=0
        self.gameover_collision=0
        self.gameoverzero=0
        arcade.set_background_color(arcade.color.KHAKI)
        


    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(self.snake.score,self.width-60,10,arcade.color.GRAY,28,16)

        if self.gameoverzero==0 and self.gameover_outfit==0 and self.gameover_collision==0:
            # self.apple.draw()
            self.poo.draw()
            self.pear.draw()
            
        if self.gameoverzero==1 or self.gameover_outfit==1 or self.gameover_collision==1:
            self.snake.change_x=0
            self.snake.change_y=0

            arcade.draw_text('GAME OVER',self.width//4,self.height//2,arcade.color.RED,28,16)
        self.gameover_collision=self.snake.draw()
        arcade.finish_render()

    

    def on_key_release(self, symbol ,modifiers):
        if symbol == arcade.key.UP:
            if self.snake.change_y!=-1:
                self.snake.change_x=0
                self.snake.change_y=1
        elif symbol== arcade.key.DOWN:
            if self.snake.change_y!=1:
                self.snake.change_x=0
                self.snake.change_y=-1
        elif symbol== arcade.key.LEFT:
            if self.snake.change_x!=1:
                self.snake.change_x=-1
                self.snake.change_y=0
        elif symbol== arcade.key.RIGHT:
            if self.snake.change_x!=-1:
                self.snake.change_x=1
                self.snake.change_y=0
        elif symbol== arcade.key.Q:
            df_input=pd.DataFrame(self.eat.data.list_input)
            df_input.to_csv('dataset/input_data.csv' ,mode='a', index=False, header=False)
            df_output=pd.DataFrame(self.eat.data.list_output)
            df_output.to_csv('dataset/output_data.csv', mode='a', index=False, header=False)
            arcade.close_window()
            arcade.exit()

    def on_update(self, delta_time):
            if self.eat.pear==0:
                self.eat.eat_pear()
            if self.eat.apple==0:
                self.eat.eat_apple()
            if self.gameover_collision==0 and self.gameover_outfit==0 and self.gameoverzero==0:
                self.gameover_outfit=self.snake.move()

            # if self.snake.center_x>self.pear.center_x:
            #     self.snake.change_x=-1
            # if self.snake.center_x<self.pear.center_x:
            #     self.snake.change_x=1
            # if self.snake.center_y>self.pear.center_y:
            #     self.snake.change_x=-1                
            # if self.snake.center_y<self.pear.center_y:
            #     self.snake.change_x=1

            if arcade.check_for_collision(self.snake,self.apple):
                self.gameoverzero=self.snake.eat(self.apple,1)
                self.eat.apple=1
                # self.eat.pear=0
                self.apple=Apple(self)
            if arcade.check_for_collision(self.snake,self.pear):   
                self.gameoverzero=self.snake.eat(self.pear,2)   
                self.eat.pear=0 
                self.eat.apple=1
                self.pear=Pear(self)
            if arcade.check_for_collision(self.snake,self.poo):
                self.gameoverzero=self.snake.eat(self.poo,3) 
                self.poo=Poo(self)


    

if __name__ == "__main__":

    game=Game()
    arcade.run()
    

