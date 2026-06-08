from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.table = Turtle()
        self.table.hideturtle()
        self.table.penup()
        self.table.color('white')
        self.table.goto(0, 280)
        self.score_game(0)

    def score_game(self, score):
        # self.table
        self.table.clear()
        self.table.write(f"Score: {score}", False, "center", ("Courier", 12, "bold"))

    def crash_wall(self, c_loc):
        if not -280 <= c_loc[0] <= 270 or not -270 <= c_loc[1] <= 280:
            self.game_over()
            return True

    def crash_tail(self, s_body):
        head = s_body[0].pos()
        for s_sec in range(3, len(s_body)):
            if s_body[s_sec].distance(head) <= 10:
                self.game_over()
                return True



    def game_over(self):
        loss = Turtle()
        loss.hideturtle()
        loss.color('white')
        loss.write("You lost!", False, "center", ("Courier", 24, "bold"))


