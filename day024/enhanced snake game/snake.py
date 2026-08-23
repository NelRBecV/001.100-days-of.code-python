from segment import Segment
from turtle import Screen


class Snake:
    def __init__(self):
        self.body = []
        self.count = 0
        self.create_snake_head()

    def create_snake_head(self):
        """Initializes the playable character of the game (the snake)."""
        for i in range(3):
            self.add_segment()

    def add_segment(self):
        """Increments the body of the snake by one piece."""
        self.body.append(Segment(self.count))
        self.count += 1

    def reset_snake_body(self, screen: Screen):
        """Returns body of the snake to its initial state."""
        self.count = 0
        for section in self.body:
            section.color('black')
            screen._turtles.remove(section)
        self.body.clear()
        self.create_snake_head()

    def moving(self):
        """Gets snake constantly moving through the game."""
        for s in range(len(self.body) - 1, 0, -1):
            pos_x = self.body[s - 1].xcor()
            pos_y = self.body[s - 1].ycor()
            self.body[s].goto(pos_x, pos_y)
        self.body[0].forward(10)

    def move_up(self):
        """Set snake's direction to UP."""
        if self.body[0].heading() != 270:
            self.body[0].setheading(90)

    def move_down(self):
        """Set snake's direction to DOWN."""
        if self.body[0].heading() != 90:
            self.body[0].setheading(270)

    def move_left(self):
        """Set snake's direction to LEFT."""
        if self.body[0].heading() != 0:
            self.body[0].setheading(180)

    def move_right(self):
        """Set snake's direction to RIGHT."""
        if self.body[0].heading() != 180:
            self.body[0].setheading(0)

    def get_head_pos(self) -> tuple:
        """Returns a tuple with x-y coordinates of snake."""
        return self.body[0].pos()

    def crash_wall(self) -> bool:
        """Checks if snake's head hits any of the walls (window borders) of the game."""
        x, y = self.get_head_pos()
        if not -280 <= x <= 270 or not -270 <= y <= 280:
            return True

    def crash_tail(self) -> bool:
        """Checks if the snake's head touches one section of its tail."""
        head_x, head_y = self.get_head_pos()
        for sec in range(3, len(self.body)):
            if self.body[sec].distance(head_x, head_y) <= 10:
                return True

    def is_crashed(self):
        """Returns 'True' if snake's head touches the walls or its own tail. Otherwise, returns 'False'."""
        return self.crash_wall() or self.crash_tail()
