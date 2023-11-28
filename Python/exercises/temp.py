from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.bgcolor("light green")
screen.colormode(255)

alex = Turtle()
alex.color("blue")
alex.width(10)
alex.shapesize(5)


def shapes():
    for i in range(3, 13):
        x = int(360 / i)
        alex.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))
        for y in range(i):
            alex.forward(70)
            alex.right(x)

def key_move_right():
    #alex.left(90)
    alex.forward(20)

def key_move_left():
    #alex.right(90)
    alex.backward(20)


def key_move_up():
    alex.left(20)
    #alex.forward(20)


def key_move_down():
    #alex.right(90)
    alex.forward(-20)



screen.listen()
screen.onkey(key="Right", fun=key_move_right)

screen.listen()
screen.onkey(key="Left", fun=key_move_left)




# shapes()
screen.exitonclick()
