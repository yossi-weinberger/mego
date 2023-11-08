import graphics
print (graphics.headline)
add_more = ""
previous_result = 0

def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b

while add_more != "exit":
    num1 = int(input("Type the first number: "))
    operator = input("Type the operator (+-*/): ")
    num2 = int(input("Type the second number: "))

    a = num1
    b = num2

    if operator =='+':
        result = (addition(a,b)) + previous_result
    if operator =='-':
        result = (subtraction(a,b)) + previous_result
    if operator =='*':
        result = (multiplication(a,b)) + previous_result
    if operator =='/':
        result = (division(a,b)) + previous_result

    print(f"The result is: {result}")
    print(f"{graphics.add_more_txt}",end="")
    add_more = input()

    if add_more == "add":
        previous_result = result
    if add_more == "c":
        previous_result = 0

#TODO: