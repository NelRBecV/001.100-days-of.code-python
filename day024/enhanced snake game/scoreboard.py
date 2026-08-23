from screen_text import ScreenText


class Scoreboard:
    def __init__(self):
        super().__init__()
        self.hs = 0
        self.score = 0
        self.file_path = "record.txt"
        self.current_score = ScreenText()
        self.high_scores = ScreenText()

    def show_score_game(self):
        self.current_score.set_pos((0, 280))
        self.current_score.set_text(f"Score: {self.score}")

    def show_highscore(self):
        self.high_scores.set_pos((220, 280))
        self.high_scores.set_text(f"Hi-score: {self.hs}")

    def increasing_points(self):
        self.score += 1

    def reset_scoreboard(self):
        try:
            with open(self.file_path, "r") as record:
                max_point: str = record.read()
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

    def game_over(self):
        ScreenText(text="You lost!", move=False, align="center", font=("Courier", 24, "bold"))
