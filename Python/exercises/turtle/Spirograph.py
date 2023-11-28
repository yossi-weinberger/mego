import turtle
from time import sleep
from turtle import Turtle, Screen
from random import randint




screen = Screen()
screen.bgcolor("lightgreen")
screen.colormode(255)


alex = Turtle()
alex.shape("turtle")
alex.color("blue")
alex.pencolor("black")
alex.width(randint(2, 5))
#alex.fillcolor("red")
alex.hideturtle()

def color_change():
    r = randint(1, 255)
    g = randint(1, 255)
    b = randint(1, 255)
    alex.color(r, b, g)
    r += 5
    if r >= 250:
        r = 0
    b += 10
    if b >= 250:
        b = 0
    g -= 5
    if g <= 5:
        g = 0


# alex.penup()
# alex.goto(-450, -300)
# alex.pendown()

def shape():
    radios = 5
    for i in range(25):
        color_change()
        alex.circle(radios,180,4)
        radios += 5

        #alex.forward(5)

for i in range (5):
    shape()
    alex.forward(10)
    alex.right(90)



# for i in range(20):
#     random_moves()
#     alex.left(5)
#     alex.forward(50)
#     random_moves()


screen.exitonclick()
