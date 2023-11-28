from turtle import Turtle
from random import randint


class Players:

    def __init__(self, name, size, color, x, y):
        self.turtle = Turtle()
        self.turtle.penup()
        self.name = name
        self.turtle.shape("turtle")
        self.turtle.shapesize(size)
        self.turtle.color(color)
        self.turtle.goto((x, y))

    def race_moving(self):
        self.turtle.forward(randint(2, 50))
