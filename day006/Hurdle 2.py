def turn_right():
    turn_left()
    turn_left()
    turn_left()

def race():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() == False:
    race()


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
