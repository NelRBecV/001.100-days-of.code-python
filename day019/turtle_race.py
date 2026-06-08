from turtle import Turtle, Screen
import random


def blue_turtle():
    leo.penup()
    leo.shape("turtle")
    leo.setposition(-300, 100)
    leo.color(25, 0, 255)


def red_turtle():
    ralph.penup()
    ralph.color(233, 13, 13)
    ralph.shape('turtle')
    ralph.setposition(-300, 50)


def orange_turtle():
    mike.penup()
    mike.color(233, 130, 13)
    mike.shape('turtle')
    mike.setposition(-300, -50)


def purple_turtle():
    don.penup()
    don.color(181, 13, 233)
    don.shape('turtle')
    don.setposition(-300, -100)


def gray_turtle():
    timmy.penup()
    timmy.color(71, 70, 70)
    timmy.shape('turtle')
    timmy.setposition(-300, 0)


def start_race():

    tmnt = [leo, ralph, timmy, mike, don]
    for tur in tmnt:
        tur.forward(random.randint(1, 5))
        if tur.xcor() > goal:
            return tur
    return None


track = Screen()
leo = Turtle()
ralph = Turtle()
timmy = Turtle()
mike = Turtle()
don = Turtle()


track.colormode(255)
blue_turtle()
red_turtle()
gray_turtle()
orange_turtle()
purple_turtle()

track.setup(height=300, width=650)
user_guess = track.textinput(title="Guess the winner", prompt="Who you think yo win? Write your option: ")
if user_guess:
    contender = {leo: "blue", ralph: 'red', timmy: 'gray', mike: 'orange', don: 'purple'}
    finish = None

    #delimit the finish line by placing it 6% less over general window width
    goal = round((track.window_width() / 2) - (track.window_width() * 0.06))

    while not finish:
        finish = start_race()

    if contender[finish] == user_guess:
        print(f"Congratulations!!! The {user_guess} won")
    else:
        print(f"The {contender[finish]} turtle won. You lost")

track.exitonclick()
