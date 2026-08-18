from turtle import Turtle


class Segment(Turtle):
    """Creates a section with a square shape."""
    def __init__(self, pos: int):
        super().__init__()
        self.speed('fastest')
        self.shape('square')
        self.penup()
        self.setx(20 * pos)
        self.color('white')
