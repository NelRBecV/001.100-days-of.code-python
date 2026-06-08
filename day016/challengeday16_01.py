from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)

my_screen = Screen()
timmy.shape('turtle')
print(my_screen.canvheight)
timmy.color('Pink')
timmy.left(65)
timmy.forward(100)
timmy.left(95)
timmy.forward(100)
timmy.right(45)
timmy.forward(100)
timmy.left(90)
timmy.right(25)
timmy.forward(150)
my_screen.exitonclick()
