import turtle as t
import time
from random import randint

# screen ---------------------------
screen = t.Screen()
screen.title("snake game")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)
screen.tracer(0)


# head ------------------------------

head = t.Turtle()
head.shape("square")
head.color('red')
head.direction = 'right'
head.penup()
head.speed('fastest')
segment = []
#--------------- food ------------------
food = t.Turtle()
food.shape("circle")
food.color('green')
food.penup()
food.speed('fastest')
food.goto(randint(-290, 290), randint(-290, 290))
def move():
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

screen.listen() # for any event! listen

def up() :
    if head.direction!= 'down' : head.direction = "up"
def down() :
    if head.direction != 'up':
        head.direction = "down"
def left() :
    if head.direction!= 'right' :
        head.direction = "left"
def right() :
    if head.direction != 'left' :
        head.direction = "right"
screen.onkeypress(up, 'w')
screen.onkeypress(down, 's')
screen.onkeypress(left, 'a')
screen.onkeypress(right, 'd')

while True:
    screen.update()
    time.sleep(0.1)
    move()
    #  ----------------wall detection -------------
    if head.xcor() > 290 or head.xcor() < -290 :
        head.setx(-head.xcor())

    if head.ycor() > 290 or head.ycor() < -290 :
        head.sety(-head.ycor())

    #  --------------- food detection--------------
    if head.distance(food) < 20 :
        food.goto(randint(-290, 290), randint(-290, 290))
        seg = t.Turtle()
        seg.color('red')
        seg.speed('fastest')
        seg.shape('square')
        seg.penup()
        segment.append(seg)
        print(segment)

    for i in range(len(segment)-1, 0, -1):
        x = segment[i-1].xcor()
        y = segment[i-1].ycor()
        segment[i].goto(x, y)

    if len(segment) > 0 :
        x = head.xcor()
        y = head.ycor()
        segment[0].goto(x,y)
