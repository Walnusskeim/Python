'''
Python turtle
Maximilian
May 2022
'''

#import
from random import *
from turtle import *


#Functions#

#Function for a square
def square(size):
    for i in range(4):
        forward(size)
        left(90)

#draw a circle
def circle2(size):
    for i in range(360):
        forward(size)
        left(1)

#function for a rectangle (Door)
def rectangle_door(size, width):
    for i in range(2):
        forward(size)
        left(90)
        forward(width)
        left(90)

#Function for a rectangle (Doorwindow)
def rectangle_doorwindow(size, width):
    for i in range(2):
        forward(size)
        left(90)
        forward(width)
        left(90)

#Moves the turtle without drawing anything
def move(x, y):
    penup()
    goto(x, y)
    setheading(0)
    pendown()

# ends fill - changes color - starts new fill
def colorchange(pencolor, fillcolor):
    end_fill()
    color(pencolor, fillcolor)
    begin_fill()

#Draws the house
def house(startx, starty, pencolor, fillcolor, scale):
    move(startx, starty)
    colorchange(pencolor, fillcolor)

    speed(500)
    square(100*scale)

    move(xcor() + 100*scale, ycor() + 100*scale)
    left(135)
    forward(70 * scale)
    left(90)
    forward(70 * scale)


    colorchange(pencolor, '#00fcf0')
    move(xcor() + 15*scale, ycor() - 30*scale)
    square(20*scale)

    colorchange(pencolor, '#00fcf0')
    move(xcor() + 50 * scale, ycor())
    square(20 * scale)

    colorchange(pencolor, '#00fcf0')
    move(xcor() -50 * scale, ycor() - 50 * scale)
    square(20 * scale)

    colorchange(pencolor, '#808080')
    move(xcor() + 50 * scale, ycor() - 20 * scale)
    rectangle_door(20 * scale, 40 * scale)

    colorchange('#fffb00', '#fffb00')
    move(xcor() + 3 * scale, ycor() + 15 * scale)
    circle(2.5 * scale)

    colorchange(pencolor, '#00fcf0')
    move(xcor() + 4.5 * scale, ycor() - 3 * scale)
    rectangle_doorwindow(5 * scale, 25 * scale)


    end_fill()


while True:
    pen = ["#" + ''.join([choice('ABCDEF0123456789') for i in range(6)])]
    back = ["#" + ''.join([choice('ABCDEF0123456789') for i in range(6)])]
    ranX = randint(50 - screensize()[0], screensize()[0] - 100)
    ranY = randint(50 - screensize()[1], screensize()[1] - 100)
    scale = uniform(0.25, 2)
    house(ranX, ranY, pen, back, scale)

