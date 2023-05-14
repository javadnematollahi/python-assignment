import arcade
from main import * 

class Snake(arcade.Sprite):
    def __init__(self,game):
        super().__init__()
        self.body=[]
        self.width=32
        self.height=32
        self.center_x=game.width//2
        self.center_y=game.height//2
        self.change_x=0
        self.change_y=0
        self.color=arcade.color.GREEN
        self.colorbody=arcade.color.BLUE
        self.speed=4
        self.score=0
        self.w=game.width
        self.h=game.height       

    def draw(self):
        
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)
        for i,part in enumerate(self.body):
            if i%2==0:
                self.colorbody=arcade.color.BLUE
            elif i%2==1:
                self.colorbody=arcade.color.GREEN
            arcade.draw_rectangle_filled(part['x'],part['y'],self.width,self.height,self.colorbody)
            if self.center_x==part['x'] and self.center_y==part['y']:
                print('collision')
                return 1
        return 0

    def move(self):
        # if  self.center_x>game.width or self.center_x<0 or self.center_y>game.height or self.center_y<0:
        #     return 1
        # else:           
            self.body.append({'x':self.center_x,'y':self.center_y})
            if len(self.body)>self.score:
                for i in range(len(self.body)-self.score):       #in halghe baraye in ast ke vaghti emtiz manfi migirim tedad tekehae badane mar be andazeye emtiz shavand. agar in halghe ra nazarim faqat ozvi ke ezafe shode hazf mishavad, dar sorati ke bayad be andazeye emtiaz manfi ham ozv kam konim
                    self.body.pop(0)

            self.center_x+=self.change_x*self.speed
            self.center_y+=self.change_y*self.speed
            if  self.center_x> self.w or self.center_x<0 or self.center_y> self.h or self.center_y<0:
                    print('outfit')
                    return 1
            return 0
        

    def eat(self,fruit,kind):
        del fruit
        if kind==1:
            self.score+=1
        elif kind==2:
            self.score+=2
        elif kind==3:
            self.score-=1
        if self.score<0 or self.score==0:
            self.score=0
            print('zeroscore')
            return 1
        else:
            return 0  