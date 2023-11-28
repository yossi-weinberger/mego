from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)
screen.bgcolor(143, 247, 204)

# screen.bgpic("D:\mego\Python\exercises\Etch A Sketch\pic.jpg")

pen = Turtle()
pen.shape("turtle")
pen.pencolor("black")
pen.width(3)
pen.shape("arrow")

#pen.hideturtle()


def pen_move_right():
    pen.right(5)


def pen_move_left():
    pen.left(5)


def pen_move_forword():
    pen.forward(5)


def pen_move_backword():
    pen.backward(5)


screen.listen()
screen.onkeypress(key="a", fun=pen_move_left)
screen.onkeypress(key="d", fun=pen_move_right)
screen.onkeypress(key="w", fun=pen_move_forword)
screen.onkeypress(key="s", fun=pen_move_backword)



screen.exitonclick()