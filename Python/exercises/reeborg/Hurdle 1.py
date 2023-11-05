def r_move():
    move()
    turn_right ()   

def l_move():
    move()
    turn_left()
    
def r2():
    for i in range (2):
        r_move()
    
def turn_right ():
    for i in range (3):
        turn_left()

def moving():
    l_move()
    r2 ()
    l_move()

for i in range(6):   
    moving ()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turn_right ():
    for i in range (3):
        turn_left()

def moveing():
    move()
    turn_left()
    move()
    turn_right ()
    move()
    turn_right ()
    
moving ()



