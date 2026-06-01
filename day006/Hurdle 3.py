def turn_right():
    turn_left()
    turn_left()
    turn_left()

def dodge():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#while at_goal() == False:
while not at_goal():#Her
    #if wall_in_front() == True: 
    if wall_in_front():#Her
        dodge()    
    else:
        move()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
