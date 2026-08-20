from turtle import Turtle


class Match:
    def __init__(self):
        self.points = [0]*2
        self.score = []
        for i in range(2):
            self.score.append(Turtle())
            self.score[i].color('white')
            self.score[i].penup()
            self.score[i].speed('fastest')
            self.score[i].setpos(-200 + (400 * i), 250)
            self.score[i].hideturtle()

    def keeping_scores(self, side):
        if side <= -510:
            self.points[1] += 1

        elif side > 510:
            self.points[0] += 1

        self.scores()

    def check_winner(self):
        for p in range(len(self.points)):
            if self.points[p] == 15:
                return p+1

    def show_winner(self):
        win = Turtle()
        win.hideturtle()
        win.color('white')
        win.penup()
        win.write(f" Game Over\nPlayer {self.check_winner()} wins", False, "center", ("EightBit Atari", 40, "normal"))

    def scores(self):
        for g_points in range(len(self.score)):
            self.score[g_points].clear()
            self.score[g_points].write(f"{self.points[g_points]}", False, "center", ('EightBit Atari', 30, 'normal'))
