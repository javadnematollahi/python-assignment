import turtle
from svg_turtle import SvgTurtle

turtle.bgcolor("white")

colors = ["red","purple","blue","green","yellow","orange"]

p = turtle.Pen("turtle")

def draw():
    for i in range(10):
        for j in range(3+i):
            if j==0:
                if i==0:
                    p.left(150)
                elif i>0:
                    p.left(180-(((1+i)*180)/((3+i)*2)))
            else:
                p.left(180-(((1+i)*180)/(3+i)))
            if i==0:
                p.forward(55)
            elif 0<i<3:
                p.forward(60+(3*i))
            else:
                p.forward(70)
        p.pencolor("white")
        if i==0:
            p.right(30)
        elif i>0:
            p.right((((1+i)*180)/((3+i)*2)))
        if i<2:
            p.forward(10)
        else:
            p.forward(10)
        p.pencolor("black")
    turtle.done()


draw()


        