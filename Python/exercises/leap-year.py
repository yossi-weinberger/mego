year = int(input("Type a year: "))
leap = " is a leap year"
not_leap = " is NOT a leap year"
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year}{leap}")
        else:
            print(f"{year}{not_leap}")
    else:
        print(f"{year}{leap}")
else:
    print(f"{year}{not_leap}")
