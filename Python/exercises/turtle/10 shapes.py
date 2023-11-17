from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.bgcolor("light green")
screen.colormode(255)

alex = Turtle()
alex.color("blue")
alex.width(10)


def shapes():
    for i in range(3, 13):
        x = int(360 / i)
        alex.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))
        for y in range(i):
            alex.forward(70)
            alex.right(x)


shapes()
screen.exitonclick()
