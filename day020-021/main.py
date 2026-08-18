from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


scn = Screen()
scn.setup(width=600, height=600)
scn.bgcolor('black')
scn.title("My own Snake Game")
my_points = 0
points = Scoreboard()
my_snake = Snake()
start = True
s_food = Food()
scn.listen()
points.score_game(my_points)

while start:
    scn.update()  # refresh display screen
    time.sleep(0.1)  # delay function "moving by 1 millisecond"
    my_snake.move_forward()
    height = scn.window_height() // 2
    width = scn.window_width() // 2
    # detect collision with the wall or tail
    if my_snake.crash_tail() or my_snake.crash_wall(width, height):
        points.game_over()
        start = False

    # detect collision with s_food (snake food)
    if s_food.is_eaten(my_snake.get_location()):
        s_food.refresh()
        my_snake.add_segment()
        my_points += 1
        points.score_game(my_points)

    scn.onkey(my_snake.move_up, "w")
    scn.onkey(my_snake.move_down, "s")
    scn.onkey(my_snake.move_left, "a")
    scn.onkey(my_snake.move_right, "d")
scn.exitonclick()
