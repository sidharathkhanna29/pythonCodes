"""
Graphics:
1) Turtle ---> Graphic design, drawings, Game (pygame)
2) Tkinter ---> GUI, forms, interfaces

event ---> any intraction user has with an interface can consider as event
even listener -->detect the event
"""

import turtle as t
from random import randint, choice

screen = t.Screen() # that creates a screen for me!
pen = t.Turtle() # this is an object from turtle
screen.setup(1000, 1000)
#pen.penup()
pen.speed('fastest')
pen.color('purple')
screen.bgcolor('gray')
listColour = ['purple', 'green', 'orange', 'red', 'cyan', 'blue']

def shape(n,size):
    for i in range(n):
        pen.forward(size)
        pen.left(360/n)

index = -1
for time in range(100):
    randX = randint(-450, 450)
    randY = randint(-450, 450)
    pen.penup()
    pen.goto(randX, randY)
    pen.pendown()
    size = randint(10, 15)
    for sh in range(8, 2, - 1):
        pen.color(choice(listColour))
        for i in range(5):
            shape(sh, size)
            pen.left(72)
        index -= 1




t.mainloop() # it loop through the screen to detect any event!

