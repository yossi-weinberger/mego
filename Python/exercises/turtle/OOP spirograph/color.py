from random import randint

class Color:

    def __init__(self,r, b, g):
        r = randint(1, 255)
        g = randint(1, 255)
        b = randint(1, 255)

    def  color_change():
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