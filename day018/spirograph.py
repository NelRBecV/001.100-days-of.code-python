import random  # Timmy the turtle
from turtle import Turtle, Screen
# import Turtle as t


def random_color():
    r = round(random.random(), 2)
    g = round(random.random(), 2)
    b = round(random.random(), 2)
    return r, g, b


# tim = t
timmy_the_turtle = Turtle()
timmy_the_turtle.screen.bgcolor('white')
timmy_the_turtle.shape('turtle')

# As I did
laps = int((360 / 6) / 2)
while (laps + 6) > 0:
    timmy_the_turtle.speed(0)
    timmy_the_turtle.left(10)
    timmy_the_turtle.circle(90, 360)
    timmy_the_turtle.pencolor(random_color())
    laps -= 1


#As she did
# def random_color():
#     r = round(random.random(), 2)
#     g = round(random.random(), 2)
#     b = round(random.random(), 2)
#     color = (r, g, b)
#     return color

# def draw_spirograph(size_of_gap):
#     for _ in range(int(360/size_of_gap)):
#         timmy_the_turtle.speed('fastest')
#         timmy_the_turtle.color(random_color())
#         timmy_the_turtle.circle(100)
#         timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)


# draw_spirograph(5)
scr_2 = Screen()
scr_2.exitonclick()
scr_2.title("Timmy the Turtle")
