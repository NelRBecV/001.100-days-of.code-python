from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        for i in range(2):
            self.hideturtle()
            self.penup()
            self.color('white')
            self.speed('fastest')
            self.shape('square')
            self.resizemode('user')
            self.shapesize(0.5, 3.0, 0.0)
            self.setheading(90)

            self.showturtle()


    def move_up(self):
        if self.ycor() < 260:
            self.forward(10)

    def move_down(self):
        if self.ycor() > -250:
            self.backward(10)
