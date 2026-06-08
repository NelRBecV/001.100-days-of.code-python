import random  # Timmy the turtle
from turtle import Turtle, Screen
# import Turtle as t


# tim = t
timmy_the_turtle = Turtle()
timmy_the_turtle.screen.bgcolor('white')
timmy_the_turtle.shape('turtle')

# As I did it
colors = ['black', 'blue', 'red', 'orange', 'brown', 'green', 'yellow', 'purple', 'gray']
timmy_the_turtle.penup()
timmy_the_turtle.setx(-100)
timmy_the_turtle.sety(100)
timmy_the_turtle.pendown()

for i in range(2, 10):  # Draw a lot of shapes
    ang = int(360 / (i + 1))
    timmy_the_turtle.pencolor(random.choice(colors))
    for j in range(i + 1):  # Draw a single shape
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(ang)

# As she did it
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# def draw_shapes(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.left(angle)
#
#
# for shape_side_n in range(3,11):
#     timmy_the_turtle.pencolor(random.choice(colors))
#     draw_shapes(shape_side_n)


src = Screen()
src.exitonclick()
src.title('Challenge Day 18')
