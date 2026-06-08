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
f_snake = Food()
scn.listen()
my_snake.body[0].write = ("Score: ", False, "center", "Times New Roman")

while start:
    scn.update()  #refresh display screen
    time.sleep(0.1)  #delay function "moving by 1 milisecond"
    my_snake.moving()
    
    #detect collision with f (food)
    pos = my_snake.body[0].pos()
    
    # detect collision with the wall or tail
    if points.crash_wall(pos): #or points.crash_tail(my_snake):
        start = False
    
    # detect collision with the tail
    if points.crash_tail(my_snake.body):
        start = False
        
    if f_snake.distance(my_snake.body[0].pos()) < 20:
        f_snake.refresh()
        my_snake.segments()
        my_points += 1
        points.score_game(my_points)


    scn.onkey(my_snake.move_up, "w")
    scn.onkey(my_snake.move_down, "s")
    scn.onkey(my_snake.move_left, "a")
    scn.onkey(my_snake.move_right, "d")
scn.exitonclick()
