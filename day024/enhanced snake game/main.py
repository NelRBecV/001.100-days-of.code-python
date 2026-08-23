from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


scn: Screen = Screen()
scn.setup(width=600, height=600)
scn.bgcolor('black')
scn.title("My own Snake Game")
points: Scoreboard = Scoreboard()
points.reset_scoreboard()
my_snake: Snake = Snake()
food_snake: Food = Food()
start: bool = True
my_points: int = 0
scn.listen()
scn.onkey(my_snake.move_up, "w")
scn.onkey(my_snake.move_down, "s")
scn.onkey(my_snake.move_left, "a")
scn.onkey(my_snake.move_right, "d")

while start:
    scn.update()  # refresh display screen
    time.sleep(0.1)  # delay function "moving by 1 millisecond"
    my_snake.moving()

    # detect collision with food
    if food_snake.is_eaten(my_snake):
        points.increasing_points()
        points.show_score_game()
        points.show_highscore()
        food_snake.refresh()
        my_snake.add_segment()

    # detect collision with the wall or its own tail
    if my_snake.is_crashed():
        points.reset_scoreboard()
        my_snake.reset_snake_body(scn)

scn.exitonclick()
