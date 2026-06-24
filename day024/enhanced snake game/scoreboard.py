from turtle import Turtle
from snake import Snake


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hs = 0
        self.score = 0
        self.high_s = Turtle()
        self.high_s.penup()
        self.high_s.goto(220, 280)
        self.high_s.color('white')
        self.high_s.hideturtle()
        self.file_path = "record.txt"

    def show_score_game(self):
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 280)
        self.write(f"Score: {self.score}", False, "center", ("Courier", 12, "bold"))

    def crash(self, snake: Snake):
        if snake.crash_wall() or snake.crash_tail():
            return True

    def reset_game(self):
        try:
            record = open(self.file_path, "r")
            max_point: str = record.read()
            record.close()
        except FileNotFoundError:
            max_point: str = "0"

        if max_point != "":
            self.hs = int(max_point)

        if self.hs < self.score:
            self.hs = self.score
            with open(self.file_path, "w") as record:
                record.write(str(self.score))

        self.score = 0

        self.show_score_game()
        self.show_highscore()

    def show_highscore(self):
        self.high_s.write(f"Hi-score: {self.hs}", False, "Center", ("Courier", 12, "bold"))

    def increasing_points(self):
        self.score += 1
        self.show_score_game()

    def game_over(self):
        loss = Turtle()
        loss.hideturtle()
        loss.color('white')
        loss.write("You lost!", False, "center", ("Courier", 24, "bold"))

    def clear_scores(self):
        self.high_s.clear()
        self.clear()
