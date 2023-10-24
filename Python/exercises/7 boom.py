for i in range (1,101):
    if i % 7 == 0:
        print("BOOM!")
    elif i % 10 == 7:
        print("BOOM!")
    elif i//10 == 7:
        print("BOOM!")    
    else:
        print (i)

