from turtle import Turtle


class Snake:
    def __init__(self):
        self.body = []
        self.count = 0

        for i in range(3):
            self.segments()


    def segments(self):
        section = Turtle()
        section.speed('fastest')
        section.shape('square')
        section.penup()
        section.setx(20 * self.count)
        section.color('white')
        self.body.append(section)
        self.count += 1

    def moving(self):
        for s in range(len(self.body) - 1, 0, -1):
            pos_x = self.body[s - 1].xcor()
            pos_y = self.body[s - 1].ycor()
            self.body[s].goto(pos_x, pos_y)

        self.body[0].forward(10)

    def move_up(self):
        if self.body[0].heading() != 270:
            self.body[0].setheading(90)

    def move_down(self):
        if self.body[0].heading() != 90:
            self.body[0].setheading(270)

    def move_left(self):
        if self.body[0].heading() != 0:
            self.body[0].setheading(180)

    def move_right(self):
        if self.body[0].heading() != 180:
            self.body[0].setheading(0)

