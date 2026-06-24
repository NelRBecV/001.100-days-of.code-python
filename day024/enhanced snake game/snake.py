from turtle import Turtle


class Snake:
    def __init__(self):
        self.body = []
        self.count = 0
        self.snake()

    def snake(self):
        for i in range(3):
            self.segments()
        return self.body

    def segments(self):
        section = Turtle()
        section.speed('fastest')
        section.shape('square')
        section.penup()
        section.setx(20 * self.count)
        section.color('white')
        self.body.append(section)
        self.count += 1

    def new_game(self):
        for bs in range(len(self.body)):
            self.body[bs].goto(800, 800)

        self.body.clear()
        self.count = 0
        self.snake()

    def moving(self):
        self.body[0].forward(10)
      
        for s in range(len(self.body) - 1, 0, -1):
            pos_x = self.body[s - 1].xcor()
            pos_y = self.body[s - 1].ycor()
            self.body[s].goto(pos_x, pos_y)

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

    def get_head_pos(self):
        return self.body[0].pos()

    def crash_wall(self):
        head = self.body[0]
        if not -280 <= head.xcor() <= 270 or not -270 <= head.ycor() <= 280:
            return True

    def crash_tail(self):
        head_x, head_y = self.body[0].pos()
        for sec in range(3, len(self.body)):
            if self.body[sec].distance(head_x, head_y) <= 10:
                return True
