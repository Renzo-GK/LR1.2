print("Hello! This is programm for LR1.2 maked by Omaraschab Guseinov")

print("Okay, lets do it anything.?")

name = str(input("What is your name? \n"))

print("Nice to meet you", name, "!")

age = int(input("How old are you? \n"))

try:
    if age >18:
        print("Wow, are you student?")
    if age <18:
        print("Wow, are you schoolchild?")

except ValueError:
    print("Woops.. try again please")