def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if not wall_on_right():
        turn_right()
    else: #wall_in_front():
        turn_left()
    if front_is_clear():
        move()
    while is_facing_north() and not wall_in_front():
        move()


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
