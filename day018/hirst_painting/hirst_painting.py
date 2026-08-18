import random
from turtle import Turtle, Screen
# from turtle import Turtle as turtle_module
# from turtle import Screen
import colorgram

RGB = (colorgram.extract('image.jpg', 30))
palette = []
for i in range(len(RGB)):
    palette.append((RGB[i].rgb.r, RGB[i].rgb.g, RGB[i].rgb.b))
  
# As I did
timmy = Turtle()
timmy.screen.colormode(255)
timmy.penup()
timmy.setpos(-250.00, -200.00)
timmy.speed(10)

for pos in range(-270, 280, 40):
    timmy.setpos(-350, pos)
    for _ in range(12):
        timmy.pencolor(random.choice(palette))
        timmy.forward(30)
        timmy.pendown()
        timmy.dot(20)
        timmy.penup()
        timmy.forward(30)
        
# As she did
# tim = turtle_module()
# tim.screen.colormode(255)
# tim.speed('fastest')
# tim.penup()
# tim.hideturtle()
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100
# for dot_counts in range(1, number_of_dots):
#     tim.dot(20, random.choice(palette))
#     tim.forward(50)
#     if dot_counts % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)

scr = Screen()
scr.exitonclick()
