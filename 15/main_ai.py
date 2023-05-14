import arcade
from apple import *
from snake import Snake

class Eatfood():
    def __init__(self,game):
        self.game_class=game
        self.direction=0
        self.apple=1
        self.pear=0
    def eat_pear(self):

        if self.direction==0:
            if self.game_class.snake.change_y==0:
                if self.game_class.snake.center_x>=485  or self.game_class.snake.center_x<=15:
                    self.direction=2
            if self.direction==0:
                if self.game_class.pear.center_x>self.game_class.snake.center_x:
                        if self.game_class.snake.change_x!=-1:
                            self.game_class.snake.change_y=0
                            self.game_class.snake.change_x=1
                            print('right')
                elif self.game_class.pear.center_x<self.game_class.snake.center_x:
                        if self.game_class.snake.change_x!=1:
                            self.game_class.snake.change_y=0
                            self.game_class.snake.change_x=-1
                            print('left')

        if self.direction==2:
            if self.game_class.snake.change_x==0:
                if self.game_class.snake.center_y>=485  or self.game_class.snake.center_y<=15:
                    self.direction=0
            if self.direction==2:
                if self.game_class.pear.center_y>self.game_class.snake.center_y:
                        if self.game_class.snake.change_y!=-1:
                            self.game_class.snake.change_x=0
                            self.game_class.snake.change_y=1
                            print('up')
                elif self.game_class.pear.center_y<self.game_class.snake.center_y:
                        if self.game_class.snake.change_y!=1:
                            self.game_class.snake.change_x=0
                            self.game_class.snake.change_y=-1  
                            print('down')
        if self.game_class.snake.change_x!=0:
            if self.game_class.pear.center_x-16<self.game_class.snake.center_x and self.game_class.snake.center_x<self.game_class.pear.center_x+16:
                    self.direction=2
        if self.game_class.snake.change_y!=0:
            if self.game_class.pear.center_y-16<self.game_class.snake.center_y and self.game_class.snake.center_y<self.game_class.pear.center_y+16:
                    self.direction=0
        
    def eat_apple(self):

            if self.direction==0:
                if self.game_class.snake.change_y==0:
                    if self.game_class.snake.center_x>=485  or self.game_class.snake.center_x<=15:
                        self.direction=2
                if self.direction==0:
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
                    if self.game_class.snake.center_y>=485  or self.game_class.snake.center_y<=15:
                        self.direction=0
                if self.direction==2:
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
        super().__init__(width=500, height=500, title="Super Snake V1")
        self.apple=Apple(self)
        self.pear=Pear(self)
        self.poo=Poo(self)
        self.snake=Snake(self)
        self.eat=Eatfood(self)
        self.gameover_outfit=0
        self.gameover_collision=0
        self.gameoverzero=0
        self.snake.score=2
        
        arcade.set_background_color(arcade.color.KHAKI)
        


    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(self.snake.score,self.width-60,10,arcade.color.GRAY,28,16)
        
        if self.gameoverzero==0 and self.gameover_outfit==0 and self.gameover_collision==0:
            self.apple.draw()
            self.poo.draw()
            self.pear.draw()
            
        if self.gameoverzero==1 or self.gameover_outfit==1 or self.gameover_collision==1:
            self.snake.change_x=0
            self.snake.change_y=0
            arcade.draw_text("GAME OVER",self.width//4,self.height//2,arcade.color.RED,28,16)
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

    def on_update(self, delta_time):
            
            # if self.eat.pear==0:
            if arcade.get_distance_between_sprites(self.snake,self.pear)<arcade.get_distance_between_sprites(self.snake,self.apple):   
                self.eat.eat_pear()
            if arcade.get_distance_between_sprites(self.snake,self.pear)>arcade.get_distance_between_sprites(self.snake,self.apple):
                self.eat.eat_apple()
            if self.gameover_collision==0 and self.gameover_outfit==0 and self.gameoverzero==0:
                self.gameover_outfit=self.snake.move()


            if arcade.check_for_collision(self.snake,self.apple):
                self.gameoverzero=self.snake.eat(self.apple,1)
                self.eat.apple=1
                self.eat.pear=0
                self.apple=Apple(self)
            if arcade.check_for_collision(self.snake,self.pear):   
                self.gameoverzero=self.snake.eat(self.pear,2)   
                self.eat.pear=1 
                self.eat.apple=0
                self.pear=Pear(self)
            if arcade.check_for_collision(self.snake,self.poo):
                self.gameoverzero=self.snake.eat(self.poo,3) 
                self.poo=Poo(self)


    

if __name__ == "__main__":
    game=Game()
    arcade.run()
    

