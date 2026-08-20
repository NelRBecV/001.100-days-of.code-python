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
        """moves turtle up if it's still alive."""
        if self.__is_alive:
            self.forward(10)

    def reset_player(self):
        """Returns player to the starting point."""
        self.goto(0, -280)
        self.setheading(90)

    def set_player_health(self, alive: bool):
        """Changes turtle status."""
        self.__is_alive = alive

    def is_crossed(self):
        """Checks if turtle successfully crossed the street."""
        return self.ycor() >= 280
