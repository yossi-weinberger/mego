from turtle import Turtle, Screen
from random import randint

angels = [0, 90, 180, 360]
angle = angels[randint(0, 3)]

screen = Screen()
screen.bgcolor("light blue")
screen.colormode(255)

alex = Turtle()
alex.pencolor("black")
alex.hideturtle()
alex.width(10)


def drunk():
    for i in range(200):
        move = randint(30, 100)
        angle = angels[randint(0, 3)]
        alex.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))
        alex.forward(move)
        alex.right(angle)


drunk()
screen.exitonclick()
