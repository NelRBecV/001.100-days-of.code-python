from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.__is_alive: bool = True
        self.hideturtle()
        self.speed('fastest')
        self.penup()
        self.shape('turtle')
        self.color('green')
        self.reset_player()
        self.showturtle()

    def move_player(self):
        if self.__is_alive:
            self.forward(10)

    def reset_player(self):
        self.goto(0, -280)
        self.setheading(90)

    def set_player_health(self, alive: bool):
        self.__is_alive = alive

    def is_crossed(self):
        return self.ycor() >= 280
