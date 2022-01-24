Complete = False

while not Complete:
    print("I'd like to know your name, age and a fun fact about yourself!\n")
    firstanswer = input("Please tell me your name, first of all")
    if type(firstanswer) != str:
        print("please try again.")
        break
    Complete = True
