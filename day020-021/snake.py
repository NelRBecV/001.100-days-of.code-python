from segments import Segment


class Snake:
    """Creates a snake, the playable character of the game."""
    def __init__(self):
        self.body = []
        self.count = 0
        for i in range(3):
            self.add_segment()

    def add_segment(self) -> None:
        """Adds a new section to the snake."""
        self.body.append(Segment(self.count))
        self.count += 1

    def get_location(self) -> tuple:
        """Returns snake's head current position."""
        return self.body[0].pos()

    def move_forward(self) -> None:
        """Moves the snake ahead."""
        for s in range(len(self.body) - 1, 0, -1):
            pos_x = self.body[s - 1].xcor()
            pos_y = self.body[s - 1].ycor()
            self.body[s].goto(pos_x, pos_y)

        self.body[0].forward(10)

    def move_up(self) -> None:
        """Changes snake's orientation to up."""
        if self.body[0].heading() != 270:
            self.body[0].setheading(90)

    def move_down(self) -> None:
        """Changes snake's orientation to down."""
        if self.body[0].heading() != 90:
            self.body[0].setheading(270)

    def move_left(self) -> None:
        """Changes snake's orientation to the left."""
        if self.body[0].heading() != 0:
            self.body[0].setheading(180)

    def move_right(self) -> None:
        """Changes snake's orientation to the right."""
        if self.body[0].heading() != 180:
            self.body[0].setheading(0)

    def crash_tail(self) -> bool:
        """Checks if snake's head touches any section of its tail."""
        for s_sec in range(3, len(self.body)):
            if self.body[s_sec].distance(self.get_location()) <= 10:
                return True
        return False

    def crash_wall(self, width: int, height: int) -> bool:
        """Checks if snake's head touches any side of window border."""
        width -= 30
        height -= 20
        # compensate unbalance measurement of inset
        if -width - 10 > self.get_location()[0] or width < self.get_location()[0]:
            return True
        if -height + 10 > self.get_location()[1] or self.get_location()[1] > height:
            return True
        return False
