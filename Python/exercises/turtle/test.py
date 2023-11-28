import turtle
from time import sleep
from turtle import Turtle, Screen
from random import randint



def coclor_change():
    alex.color(randint(1, 255), randint(1, 255), randint(1, 255))

screen = Screen()
screen.bgcolor("lightgreen")
screen.colormode(255)


alex = Turtle()
#alex.shape("turtle")
alex.color("blue")
alex.pencolor("black")
alex.width(randint(2,20))

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
        coclor_change()

def random_moves():
    move = randint(1,20)
    angle = randint(1,20)
    for i in range(27):
        alex.forward(move)
        alex.right(angle)
        move +=1
        angle += 1
        coclor_change()

for i in range(20):
    random_moves()
    alex.left(5)
    alex.forward(50)
    random_moves()


# for i in range(20):
#     circle()
#     alex.left(5)
#     alex.forward(50)
#     circle()

# for i in range (60):
#     alex.forward(2)
#     alex.penup()
#     alex.forward(2)
#     alex.pendown()


screen.exitonclick()