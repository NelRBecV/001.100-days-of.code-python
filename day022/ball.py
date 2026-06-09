from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.resizemode('user')
        self.shapesize(1.0, 1.0, 3.0)
        self.move_y = 1
        self.penup()

    def move(self, x_move, y_move):

        if self.ycor() >= 290:
            self.move_y = -1

        if self.ycor() <= -280:
            self.move_y = 1

        x = self.xcor() + x_move
        y = self.ycor() + (self.move_y * y_move)

        self.goto(x, y)

    def reset_position(self,x,y):
        self.hideturtle()
        self.goto(x, y)
        self.showturtle()
      
