def turn_right():
    turn_left()
    turn_left()
    turn_left()
      
bucle = 0
while not at_goal():
    while is_facing_north() and front_is_clear():
            move()
    if not wall_on_right():
        turn_right()
        bucle = bucle + 1
        if bucle ==20:
            turn_right()
    else: #wall_in_left:
        turn_left()
    if front_is_clear():
        move()
                              
            
                
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
