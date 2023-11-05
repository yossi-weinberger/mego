def turn_right():
    for i in range(3):
        turn_left()
        
def r_move():
    turn_right()
    move()    

def l_move():
    turn_left()
    move()     
    
def hop():
    l_move()
    r_move()
    r_move()
    turn_left()

def move_forward():
    if front_is_clear():
        move()
    else:
        hop()
        
while not at_goal(): 
    move_forward()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turn_right():
    for i in range(3):
        turn_left()

def hop():
    turn_left()
    move()
    turn_right ()
    move()
    turn_left()        
        
def move_front():
    if front_is_clear():
        move()
    else:
        hop()
    