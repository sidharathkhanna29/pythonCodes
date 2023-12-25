
from turtle import *
from random import randint, choice

screen = Screen()
penup()
# 15 lines in parallel
goto(-240, 280)
pendown()
right(90)
steps = 20
speed('fastest')
for step in range(15):
    write(step, align='center')
    for step in range(5):
        pendown()
        forward(75)
        penup()
        forward(25)
    penup()
    goto(xcor() + 30, 280)
listTurtle = []
listColour = ['purple', 'green', 'orange', 'red', 'cyan', 'blue']

for i in range(5):
    t1 = Turtle()
    t1.color(listColour[i])
    t1.shape('turtle')
    t1.shapesize(2)
    listTurtle.append(t1)
x = 0

for t in listTurtle:
    t.penup()
    t.goto(-280 , 250 -  x)
    x += 100

end = xcor()
import  time
while True:
    time.sleep(0.5)
    t = choice(listTurtle)
    t.setx(t.xcor() + 20)
    if t.xcor() > end:
        break



mainloop()