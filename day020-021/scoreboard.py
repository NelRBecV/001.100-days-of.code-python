from turtle import Turtle


class Scoreboard:
    """Creates an object to display relevant information about the game."""
    def __init__(self):
        super().__init__()
        self.table = Turtle()
        self.table.hideturtle()
        self.table.penup()
        self.table.color('white')
        self.table.goto(0, 280)
        self.loss = Turtle()
        self.loss.hideturtle()
        self.score_game(0)

    def score_game(self, score) -> None:
        """Displays the player current score."""
        self.table.clear()
        self.table.write(f"Score: {score}", False, "center", ("Courier", 12, "bold"))

    def game_over(self) -> None:
        """Displays a message indicating player the game has ended."""
        self.loss.color('white')
        self.loss.write("You lost!", False, "center", ("Courier", 24, "bold"))
