import random  # Timmy the turtle
from turtle import Turtle, Screen
# import Turtle as t


# As I did
def random_color():
    red = round(random.random(), 2)
    green = round(random.random(), 2)
    blue = round(random.random(), 2)
    r_color = (red, green, blue)
    return r_color

def random_walk():
    if random.randint(1, 2) == 1:
        timmy_the_turtle.left(90)
    else:
        timmy_the_turtle.right(90
        


# tim = t
#
laps = 0
timmy_the_turtle = Turtle()
timmy_the_turtle.screen.bgcolor('white')
timmy_the_turtle.shape('turtle')
timmy_the_turtle.pensize(10)
while laps < 500:
    laps += 1
    color = random_color()
    timmy_the_turtle.pencolor(color[0], color[1], color[2])
    random_walk()
    timmy_the_turtle.forward(25)


#As she did it
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270]
# timmy_the_turtle = Turtle()
# timmy_the_turtle.screen.bgcolor('white')
# # timmy_the_turtle.screen.colormode(255) Change color system to RGB(255,255,255)
# timmy_the_turtle.shape('turtle')
# timmy_the_turtle.speed(0)
# timmy_the_turtle.pensize(15)
# for _ in range(200):
#     timmy_the_turtle.color(random.choice(colors))
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(directions))

scr_2 = Screen()
scr_2.exitonclick()
scr_2.title("Timmy the Turtle")
