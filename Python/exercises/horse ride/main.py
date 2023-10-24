hight = int(input("Please insert your hight in cm: "))

if hight < 120:
    print("You can't ride")
else:
    age = int(input("Please insert your age: "))
    if age < 12:
        print("You nedd to pay 5$")
    elif age >= 12 and age <= 18:
        print("You nedd to pay 7$")
    else:
        print("You nedd to pay 12$")
