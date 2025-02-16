#Part 1
print("Hello! This is programm for LR1.2 maked by Omaraschab Guseinov")
print("Okay, lets do anything")

#Part 2
name = str(input("What is your name? \n"))
print("Nice to meet you", name, "!")

#Part 3
age = int(input("How old are you? \n"))

try:
    if age >18:
        def get_yes_no_1(promt):
            while True:
                response = input(promt).strip().lower()
                if response in ["yes", "да"]:
                    return True
                elif response in ["no", "нет"]:
                    return False
                else:
                    print("Woops.. try again please")
        
        if get_yes_no_1("Wow, are you student? (yes/no): "):
            print("Good!")
        else:
            print("Hmm.. okay")

    if age <18:
        def get_yes_no_2(promt2):
            while True:
                response = input(promt2).strip().lower()
                if response in ["yes", "да"]:
                    return True
                elif response in ["no", "нет"]:
                    return False
                else:
                    print("Woops.. try again please")
        
        if get_yes_no_2("Wow, are you schoolchild? (yes/no): "):
            print("Good!")
        else:
            print("Hmm.. okay")

except ValueError:
    print("Woops.. try again please")

#Part 4
print("Okay, it is done")
