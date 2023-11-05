def turn_right():
    for i in range (3):
        turn_left()        
        
def move_forword():
    steps = 0 
    while not at_goal():
        if right_is_clear():
          if steps < 20: #to exit loops (edge cases)
               turn_right()
               move()
               steps += 1
          else:
               turn_right()
               move()
               move() 
        elif front_is_clear():
            move()
        else:
            turn_left()
            
move_forword()            
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
steps = 0
def turn_right():
    for i in range (3):
        turn_left()        
        
while not at_goal():
    if right_is_clear():
      if steps < 20:  
           turn_right()
           move()
           steps += 1
      else:
           turn_right()
           move()
           move() 
    elif front_is_clear():
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()            