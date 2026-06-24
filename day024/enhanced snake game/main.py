from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


scn: Screen = Screen()
scn.setup(width=600, height=600)
scn.bgcolor('black')
scn.title("My own Snake Game")
my_points: int = 0
points: Scoreboard = Scoreboard()
my_snake: Snake = Snake()
start: bool = True
food_snake: Food = Food()

scn.listen()
points.reset_game()
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
        points.clear_scores()
        food_snake.refresh()
        my_snake.segments()
        points.increasing_points()

    # detect collision with the wall or its own tail
    if points.crash(my_snake):
        points.reset_game()
        my_snake.new_game()    
  
scn.exitonclick()
