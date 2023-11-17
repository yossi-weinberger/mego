import turtle
from time import sleep
from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("lightgreen")

alex = Turtle()
#alex.shape("turtle")
alex.color("blue")
alex.pencolor("black")

def circle():
    move = 1
    angle = 1
    for i in range(27):
        alex.forward(move)
        #alex.penup()
        alex.right(angle)
        #alex.pendown()
        #sleep(0.1)
        move +=1
        angle += 1

for i in range(20):
    circle()
    alex.left(5)
    alex.forward(50)
    circle()

# for i in range (60):
#     alex.forward(2)
#     alex.penup()
#     alex.forward(2)
#     alex.pendown()


screen.exitonclick()