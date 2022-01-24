Complete = False

while not Complete:
    print("I'd like to know your name, age and your favourite colour!\n")
    firstAnswer = input("Please tell me your name, first of all.\n")
    if firstAnswer.isalpha():
        print("That's a nice name!")
        secondAnswer = input("Could you tell me your age now, please? Only numbers now :)\n")
        if not secondAnswer.isalpha() and 120 > int(secondAnswer) >= 0:
            print("Great!")
            finalAnswer = input("This is the final question, what is your favourite colour?\n")
            if finalAnswer.isalpha():
                print("Fantastic!\n")
                print("So, your name is " + firstAnswer.capitalize() + ", you're " + secondAnswer + " years old and your favourite colour is " + finalAnswer + "! Nice to meet you :)")
                Complete = True
            else:
                print("Your favourite colour can't be a number! Use your words! Let's start over.\n\n")
        else:
            print("Either your answer is ridiculous or wasn't numeric. Let's start from scratch.\n")
    else:
        print("please try again. Names have only alphabetic letters in them!\n")
