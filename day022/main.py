import random
from match import Field
from turtle import Screen
from paddle import Paddle
from ball import Ball


field = Screen()
field.colormode(255)
field.bgcolor('black')
field.setup(width=1000, height=600)
field.tracer()
field_elements = Field()
field_elements.net()
field_elements.scores()
field.listen()
winner = False
paddle1 = Paddle(-480, 0)
paddle2 = Paddle(475, 0)
play_ball = Ball()
speed_x = 1
speed_y = 1
while not winner:
    play_ball.set_position(0, 0)
    field.update()
    while -520 < play_ball.xcor() < 520:
        if paddle1.impact_ball(play_ball):
            speed_x = random.randint(1, 10)
            speed_y = random.randint(1, 10)

        elif paddle2.impact_ball(play_ball):
            speed_x = random.randint(1, 10) * -1
            speed_y = random.randint(1, 10)

        play_ball.move(speed_x, speed_y)

        field.onkeypress(paddle1.move_up, "w")
        field.onkeypress(paddle2.move_up, "Up")
        field.onkeypress(paddle1.move_down, "s")
        field.onkeypress(paddle2.move_down, "Down")

    field_elements.keeping_scores(play_ball.xcor())
    winner = field_elements.check_winner()

field.exitonclick()
