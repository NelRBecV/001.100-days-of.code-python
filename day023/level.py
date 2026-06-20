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
        for i in range(20):
            self.enemies_level.append(Car())

    def move_enemies(self):
        for car in self.enemies_level:
            car.move_forward(self.player_score)

    def scoreboard(self):
        self.scoreb.clear()
        self.scoreb.write(f"Level: {self.player_score}", False, "left",
                          ("EightBit Atari", 10, "normal"))

    def increment_scoreboard(self):
        self.player_score += 1

    def is_endgame(self, player: Turtle):
        for car in self.enemies_level:
            if car.hit_turtle(player):
                self.g_over.write("GAME OVER!", False, "center",
                                  ("Arial", 30, "bold"))
                return True

        return False
