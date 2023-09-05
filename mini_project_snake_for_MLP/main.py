import arcade
from apple import *
from snake import Snake


class Game(arcade.Window):

    def __init__(self):
        super().__init__(width = 500, height = 500, title = "Super Snake V1")
        self.apple = Apple(self)
        self.pear = Pear(self)
        self.poo = Poo(self)
        self.snake = Snake(self)
        self.gameover_outfit = 0
        self.gameover_collision = 0
        self.gameoverzero = 0
        arcade.set_background_color(arcade.color.KHAKI)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(text = self.snake.score, start_x = self.width-6, start_y = 10, color = arcade.color.GRAY, font_size = 28, width = 16)
        if self.gameoverzero == 0 and self.gameover_outfit == 0 and self.gameover_collision == 0:  
            self.apple.draw()
            self.poo.draw()
            self.pear.draw()
        if self.gameoverzero == 1 or self.gameover_outfit == 1 or self.gameover_collision == 1:
            arcade.draw_text( 'GAME OVER', self.width//4, self.height//2 , arcade.color.RED, 28, 16)
            arcade.draw_text( f'Your score:{self.snake.score}', 135, 200, arcade.color.RED, 28, 16)
            self.snake.change_x = 0
            self.snake.change_y = 0
            # arcade.draw_text("GAME OVER",self.width//4,self.height//2,arcade.color.RED,28,16)Your score:{self.snake.score}
        self.gameover_collision = self.snake.draw()
        arcade.finish_render()

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.UP:
            if self.snake.change_y != -1:
                self.snake.change_x = 0
                self.snake.change_y = 1
        elif symbol == arcade.key.DOWN:
            if self.snake.change_y != 1:
                self.snake.change_x = 0
                self.snake.change_y = -1
        elif symbol == arcade.key.LEFT:
            if self.snake.change_x != 1:
                self.snake.change_x = -1
                self.snake.change_y = 0
        elif symbol == arcade.key.RIGHT:
            if self.snake.change_x != -1:
                self.snake.change_x = 1
                self.snake.change_y = 0

    def on_update(self, delta_time):
            if self.gameover_collision == 0 and self.gameover_outfit == 0 and self.gameoverzero == 0:
                self.gameover_outfit = self.snake.move()
            if arcade.check_for_collision(self.snake, self.apple):
                self.gameoverzero = self.snake.eat(self.apple, 1)
                self.apple = Apple(self)
            if arcade.check_for_collision(self.snake, self.pear):   
                self.gameoverzero = self.snake.eat(self.pear, 2)    
                self.pear = Pear(self)
            if arcade.check_for_collision(self.snake, self.poo):
                self.gameoverzero = self.snake.eat(self.poo, 3) 
                self.poo = Poo(self)


if __name__ == "__main__":
    game=Game()
    arcade.run()
    

