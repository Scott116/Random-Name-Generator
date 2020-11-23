from turtle import *

from random import *

bg=Screen()
bg.setup(500,500)
bg.bgcolor("black")
colormode(255)

def randomcolor():
    red=randint(0,255)
    green=randint(0,255)
    blue=randint(0,255)
    color(red,green,blue)


def randomplace():
    penup()
    x=randint(-500,500)
    y=randint(-500,500)
    goto(x,y)
    pendown()


def randomheading():
    number=randint(1,360)
    setheading(number)


def drawrectangle():
    randomcolor()
    randomplace()
    hideturtle()
    length=randint(10,200)
    height=randint(10,200)
    begin_fill()
    forward(length)
    right(90)
    forward(height)
    right(90)
    forward(length)
    right(90)
    forward(height)
    right(90)
    end_fill()

def drawsquare():
    randomcolor()
    randomplace()
    hideturtle()
    side=randint(50,150)
    begin_fill()
    for sides in range(4):
        forward(side)
        right(90)
    end_fill()

def writescott():
    randomcolor()
    randomplace()
    hideturtle()
    style=("Times",30,"bold")
    write("SCOTT",font=style,align="center")

    

speed(10)



for i in range(50):
    writescott()
