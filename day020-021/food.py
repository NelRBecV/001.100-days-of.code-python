import random
from turtle import Turtle


class Food(Turtle):
    """Creates the snake's food."""
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed('fastest')
        self.refresh()

    def is_eaten(self, pos: tuple) -> bool:
        """Checks if food was eaten or is still in game."""
        return self.distance(pos) < 20

    def refresh(self) -> None:
        """Updates current food position."""
        self.goto(random.randint(-280, 280, ), random.randint(-280, 280))
