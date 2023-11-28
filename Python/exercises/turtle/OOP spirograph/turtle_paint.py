from turtle import Turtle, Screen
from random import randint
class Turtle_paint:
    def __init__(self):
        self.turtle = Turtle()


    def screen (self):
        self = Screen()
        self.bgcolor("lightgreen")
        self.colormode(255)

    def turtle_color(self):
        self.shape("turtle")
        self.width(randint(2, 5))
        self.hideturtle()

    def color_change(self):
        r = randint(1, 255)
        g = randint(1, 255)
        b = randint(1, 255)
        self.color(r, b, g)
        r += 5
        if r >= 250:
            r = 0
        b += 10
        if b >= 250:
            b = 0
        g -= 5
        if g <= 5:
            g = 0
