rom turtle import Turtle


class Field:
    def __init__(self):
        self.points1 = 0
        self.points2 = 0
        self.score = []
        for i in range(3):
            self.score.append(Turtle())

        for i in range(len(self.score) - 1):
            self.score[i].color('white')
            self.score[i].penup()
            self.score[i].speed('fastest')
            self.score[i].setpos(-200 + (400 * i), 250)
            self.score[i].hideturtle()

    def keeping_scores(self, side):
        if side <= -510:
            self.points2 += 1

        elif side > 510:
            self.points1 += 1

        self.scores()

    def check_winner(self):
        if self.points1 == 15:
            player = 1
            self.show_winner(player)
            return True

        if self.points2 == 15:
            player = 2
            self.show_winner(player)
            return True
        return False

    def show_winner(self, player):
            win = Turtle()
            win.hideturtle()
            win.color('white')
            win.penup()
            win.write(f" Game Over\nPlayer {player} wins", False, "center", ("EightBit Atari", 40, "normal"))

    def scores(self):
        self.score[0].clear()
        self.score[0].write(f"{self.points1}", False, "center", ('EightBit Atari', 30, 'normal'))
        self.score[1].clear()
        self.score[1].write(f"{self.points2}", False, "center", ('EightBit Atari', 30, 'normal'))

    def net(self):
        net_g = Turtle()
        net_g.hideturtle()
        net_g.color('white')
        net_g.penup()
        net_g.shape('square')
        net_g.resizemode('user')
        net_g.setpos(0, 500)
        net_g.setheading(270)
        net_g.shapesize(0.5, 1.0, 0.5)
        net_g.pensize(4)

        for i in range(40, -40, -1):
            net_g.forward(10)
            if i % 2 == 0:
                net_g.pendown()
            else:
                net_g.penup()
