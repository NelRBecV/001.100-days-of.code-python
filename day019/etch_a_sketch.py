'''
Press 'W' to move forward
Press 'S' to move backward
Press 'A' to move left
Press 'D' to move right
Press 'C' to erase what you drew 
'''

from turtle import Turtle, Screen


def move_forward():
    pencil.forward(10)


def move_backward():
    pencil.backward(10)


def move_left():
    move_forward()
    pencil.left(20)


def move_right():
    move_forward()
    pencil.right(20)


def clear_scn():
    pencil.penup()
    pencil.clear()
    pencil.home() 
    pencil.pendown()


pencil = Turtle()
board = Screen()
board.listen()
board.title("Python's Etch-A-Sketch")
board.onkey(move_forward, 'w')
board.onkey(move_backward, 's')
board.onkey(move_left, 'a')
board.onkey(move_right, 'd')
board.onkey(clear_scn, 'c')


board.exitonclick()
