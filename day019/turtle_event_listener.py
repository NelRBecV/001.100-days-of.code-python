from turtle import Turtle, Screen


def move_forward():
    timmy.forward(10)


timmy = Turtle()
scr = Screen()

scr.listen()
scr.onkey(move_forward, 'space')


scr.exitonclick()
