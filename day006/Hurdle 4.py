def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
        if not wall_on_right():
            turn_right()
    else: #wall_in_front():
        turn_left()
        


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
