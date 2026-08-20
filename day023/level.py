from turtle import Turtle
from car import Car


class Level:
    def __init__(self):
        super().__init__()
        self.enemies_level: list = []
        self.scoreb = Turtle()
        self.scoreb.hideturtle()
        self.scoreb.penup()
        self.scoreb.color('black')
        self.scoreb.goto(-270, 280)
        self.g_over = Turtle()
        self.g_over.hideturtle()
        self.player_score = 1

    def enemies(self):
        """creates enemies for the current level."""
        for i in range(20):
            self.enemies_level.append(Car())

    def move_enemies(self):
        """Adds the ability to move for every single car in game."""
        for car in self.enemies_level:
            car.move_forward(self.player_score)

    def scoreboard(self):
        """Shows scoreboard of the game."""
        self.scoreb.clear()
        self.scoreb.write(f"Level: {self.player_score}", False, "left",
                          ("EightBit Atari", 10, "normal"))

    def increment_scoreboard(self):
        """Adds up to one point each time turtle steps forward."""
        self.player_score += 1

    def is_endgame(self, player: Turtle):
        """Checks if the turtle was hit bya any car."""
        for car in self.enemies_level:
            if car.hit_turtle(player):
                self.g_over.write("GAME OVER!", False, "center",
                                  ("Arial", 30, "bold"))
                return True
        return False
