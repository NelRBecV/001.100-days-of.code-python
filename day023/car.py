from turtle import Turtle
import random

COLOR = ['blue', 'red', 'yellow', 'gray', 'purple',
         'pink', 'brown', 'orange', 'black', 'violet']


class Car(Turtle):
    def __init__(self):
        super().__init__()
        coord_x = random.randint(-26, 26) * 10
        coord_y = random.randint(-25, 26) * 10
        car_color = COLOR[random.randint(0, 9)]
        self.hideturtle()
        self.penup()
        self.shape('square')
        self.speed(10)
        self.setheading(180)
        self.goto(coord_x, coord_y)
        self.color(car_color)
        self.resizemode('user')
        self.shapesize(1, 2, 0)
        self.showturtle()

    def move_forward(self, car_speed: int):
        if self.xcor() < -300:
            self.setx(280)
        else:
            self.forward(car_speed * 10)
            self.speed('fastest')

    def hit_turtle(self, player: Turtle):
        if abs(self.xcor() - player.xcor()) <= 25 and abs(self.ycor() - player.ycor()) <= 20:
            return True

        return False
