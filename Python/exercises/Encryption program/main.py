import graphics

program_on = "y"


# is uppercase
def u_encryption():
    for i in range(len(text)):
        if (ord(text[i]) + offset) > 122:
            code = ord(text[i]) + offset - 26
            decode = chr(code)
            print(decode, end="")
        else:
            code = ord(text[i]) + offset
            decode = chr(code)
            print(decode, end="")


def u_decryption():
    for i in range(len(text)):
        if (ord(text[i]) - offset) < 97:
            code = ord(text[i]) - offset + 26
            decode = chr(code)
            print(decode, end="")
        else:
            code = ord(text[i]) - offset
            decode = chr(code)
            print(decode, end="")


# is lowercase
def l_encryption():
    for i in range(len(text)):
        if (ord(text[i]) + offset) > 90:
            code = ord(text[i]) + offset - 26
            decode = chr(code)
            print(decode, end="")
        else:
            code = ord(text[i]) + offset
            decode = chr(code)
            print(decode, end="")


def l_decryption():
    for i in range(len(text)):
        if (ord(text[i]) - offset) < 65:
            code = ord(text[i]) - offset + 26
            decode = chr(code)
            print(decode, end="")
        else:
            code = ord(text[i]) - offset
            decode = chr(code)
            print(decode, end="")


print(graphics.headline)

while program_on == "y":
    choice = int(input("Hi and wellcome to the cypher program,"
                       "\nto encryp press: 1\nto decryp press: 2\n\n"))

    text = input("Type the message:")
    offset = int(input("Type the offset: "))

    if text.isupper() == False:
        if choice == 1:
            u_encryption()
        if choice == 2:
            u_decryption()
    elif text.isupper() == True:
        if choice == 1:
            l_encryption()
        if choice == 2:
            l_decryption()
    program_on = input("\nDoy you want to continue? (y/n): ")