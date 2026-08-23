import random
from turtle import Turtle
from snake import Snake


class Food(Turtle):

    def __init__(self):
        """Creates a object that represents snake's food."""
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        """Relocates snake's food once this was eaten by it."""
        self.goto(random.randint(-280, 280, ), random.randint(-280, 280))

    def is_eaten(self, snake: Snake):
        """Returns True if this food was eaten by the snake. False if it is still in game."""
        return self.distance(snake.get_head_pos()) < 18
