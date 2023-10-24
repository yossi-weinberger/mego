print("Hi, and wellcome to the BMI calculater")

#input
age = int(input("Please enter your Age: "))
height = float(input("Please enter your Height: "))
weight = float(input("Please enter your Weight: "))

#vars
text = "Your BMI is: "
under = "You are Underweight"
normal = "Your weight is normal"
over = "You are Overweight"
obesity = "You are Obese"

#format
bmi = weight/(height ** 2)
formatted_bmi = "{:.2f}".format(bmi)

#output
if age < 65:
    if bmi < 18.5:
        print(f"{text} {formatted_bmi} {under}")
    elif bmi >= 18.5 and bmi < 24.9:
        print(f"{text} {formatted_bmi} {normal}")
    elif bmi >= 25 and bmi < 29.9:
        print(f"{text} {formatted_bmi} {over}")
    elif bmi > 30:
        print(f"{text} {formatted_bmi} {obesity}")
elif age > 65 and age < 75:
    if bmi < 22:
        print(f"{text} {formatted_bmi} {under}")
    elif bmi >= 22 and bmi < 26.9:
        print(f"{text} {formatted_bmi} {normal}")
    elif bmi >= 27 and bmi < 29.9:
        print(f"{text} {formatted_bmi} {over}")
    elif bmi > 30:
        print(f"{text} {formatted_bmi} {obesity}")
elif age > 75:
    if bmi <= 23:
        print(f"{text} {formatted_bmi} {under}")
    elif bmi >= 23.09 and bmi < 27.9:
        print(f"{text} {formatted_bmi} {normal}")
    elif bmi >= 28 and bmi < 29.9:
        print(f"{text} {formatted_bmi} {over}")
    elif bmi > 30:
        print(f"{text} {formatted_bmi} {obesity}")
