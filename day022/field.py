from turtle import Turtle


class Field(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.shape('square')
        self.resizemode('user')
        self.setpos(0, 500)
        self.setheading(270)
        self.shapesize(0.5, 1.0, 0.5)
        self.pensize(4)

        for i in range(40, -40, -1):
            self.forward(10)
            if i % 2 == 0:
                self.pendown()
            else:
                self.penup()
