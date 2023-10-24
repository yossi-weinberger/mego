import graphics
import txt
"\n\n"

#headline and intro
print(f"{graphics.game_name} \n{txt.you} \n{graphics.player}")
name = input("Type your name please: ")
print(f"nice to have you {name}\n\n")

#join or exit
print(f"{graphics.mego_ad}\n{txt.mego_ad}")
join = input("Do you wont to join? (y/n) ")

if join == "n":
    print("its a shame, go back to your lame DayJob")
    exit()
else:
    print("Nice, go to the fitting test")

#fitting test
print(f"{graphics.pc}\n{txt.test}")

#question no.1
print(f" {txt.q1} {graphics.q1p}")
points = 0
a1 = input("Type the answer: ")
if a1 == "7":
    print("Correct!")
    points += 1
else:
    print("Wrong answer!") 

#question no.2
print(txt.q2)
a2 = input("Type the answer: ")
if a2 == "3":
    print("Correct!")
    points += 1
else:
    print("Wrong answer!") 

#question no.3
print(txt.q3)
a3 = input("Type the answer: ")
if a3 == "2":
    print("Correct!")
    points += 1
else:
    print("Wrong answer!")    

#question no.4
print(f"{graphics.q4p}\n {txt.q4}")
a4 = input("Type the answer: ")
if a4 == "4":
    print("Correct!")
    points += 1
else:
    print("Wrong answer!")    

# fitting test results 
if points <= 2:
    print(f"{txt.total_points} {points} \n{txt.fail}")
    exit()
else:
    print(f"{txt.total_points} {points}\n {txt.success}")
    
    
