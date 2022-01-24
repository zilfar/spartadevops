noInput = True # have boolean that i can change to break out of while loop
theGame = False # super secret high technology variable (don't look into it if you value your life)
XENO = "---------------------------------------- "
def xenoPrint(str):

    print(XENO + str)
def xenoInput(str):
    return input(XENO + str + "\n" + XENO)

def xenoPrintOver(str):
    sys.stdout.write('\r' + XENO + str)

def xenoNL():
    print(XENO)



while True:
    print("a secret experimental version of fizzbuzz has escaped area 51 and we're looking for patients brave enough to try and figure it out")
    yesorno = input('are you up to the task? Y/N\n').strip()
    if yesorno.upper() == "Y":
        xenoPrint("you have entered the xenobuzz")
        theGame = True
        noInput = False
        break
    elif yesorno.upper() == "N":
        print("you are weak but this is to be expected.\nenjoy your disturbingly regular rendition of fizzbuzz...")
        break
    else:
        print("idk what ur trying to write but it's not Y or N, try again")



# keep looping if i haven't changed my boolean yet
while noInput:

    # ask user to put in a starting and final number to play fizzbuzz to

    rangeS = input("from what number would you like to begin fizzbuzz from\n")
    rangeF = input("up to what final number would you like to play fizzbuzz\n")

    # make sure user input is an integer which is larger than 0 and start point is lower than end
    if (rangeF.isnumeric() and int(rangeF) > 0) and (rangeS.isnumeric() and int(rangeS) < int(rangeF)):

        # ask user for first word to use instead of fizz
        firstWord = input('next, add an alternative word for \'fizz\', leave it empty to keep fizz.\n').upper()

        # check if the length of the word (after stripping whitespace) is at least 1 char, and check if it's only
        # using alphabetical chars
        if len(firstWord.strip()) < 1 or not firstWord.isalpha():

            # if they violate the rules they don't deserve to have their own word
            print('seems dodgy so i\'m just using fizz for the first word')
            # so we use fizz as the default
            firstWord = 'FIZZ'

        # ask user for second word to use instead of buzz
        secondWord = input('next, add a second alternative word for \'buzz\', leave it empty to keep buzz.\n').upper()

        # check if the length of the word (after stripping whitespace) is at least 1 char, and check if it's only
        # using alphabetical chars
        if len(secondWord.strip()) < 1 or not secondWord.isalpha():

            # if they violate the rules they don't deserve to have their own word
            print('seems dodgy so i\'m just using buzz for the first word')
            # so we use buzz as the default
            secondWord = 'BUZZ'

        # after everything is done, all the variables have a right value we can change this boolean to break out of
        # the while loop and continue onto our game
        noInput = False

    # oh and if they give a bad answer for the range then just make them try again
    else:
        # at least you get to try again this time instead of having a default value
        print('you gave a weird response idk try again')

# iterate over a loop that contains numbers from starting input number up to the final input number (+1 because end
# range isn't inclusive!!!)
if not theGame:
    for x in range(int(rangeS), int(rangeF)+1):
        # if they're a factor of 3 and 5 then by simplification they're also a factor of 15, makes it easier to write,
        # so we bring out the fizzbuzz
        if x % 15 == 0: print("waaa")

        # otherwise, check if it's at least a factor of 3, then bring out the fizz
        elif x % 3 == 0: print(firstWord)

        # if not then it could be a factor of 5, which brings out the buzz
        elif x % 5 == 0: print(secondWord)

        # otherwise just print the normal number down since they don't fit into the 3 and 5s
        else: print(x)
else:
    import time
    import keyboard
    import sys
    from threading import Thread
    xenoPrint("the Xenobuzz attacks in multiples of 3 and 5")
    xenoPrint("you must hold back the xenobuzz infiltration, you are the last line of defense and if you don't block them in time you will doom the planet yada yada")
    while True:
        xenoNL()
        menuInput = xenoInput("enter 'C' for controls, 'S' to start the game and 'F' to exit the game.")
        if menuInput.upper() == "C":
            xenoNL()
            xenoPrint('Once the game begins, you have to press buttons in accordance with whether they will be a regular enemy ("S"),')
            xenoPrint('a xeno enemy which is a multiple of 3 ("Q"), a buzz enemy which is a multiple of 5 ("E") or the dreaded xenobuzz which is a multiple of both 3 and 5 ("W")')
            xenoPrint('however, the xenobuzz are feared mainly because of how fast their attacks ramp up, and it could get overwhelming really quickly.')
        elif menuInput.upper() == "S":
            counterL = 1
            notLost = True
            while notLost:
                if counterL % 15 == 0:
                    key_pressed = False
                    wkey_pressed = False
                    roundOver = False
                    def detect_key_pressW():
                        global key_pressed
                        while not keyboard.is_pressed('w'):
                            pass
                        key_pressed = True

                    def detect_key_pressO():
                        global wkey_pressed
                        while not keyboard.is_pressed('q') and not keyboard.is_pressed('s') and not keyboard.is_pressed('e') and not roundOver:
                            pass
                        wkey_pressed = True

                    while True:
                        threadW = Thread(target=detect_key_pressW)
                        threadW.start()
                        threadO = Thread(target=detect_key_pressO)
                        threadO.start()
                        incrementSleep = (4 / (counterL ** (1 / 10))) / 10
                        for i in range(11):
                            xenoPrintOver('--' * (10-i))
                            time.sleep(incrementSleep)
                            if wkey_pressed:
                                notLost = False
                                break
                            elif key_pressed:
                                wkey_pressed = False
                                roundOver = True
                                break
                            elif i == 10 and not key_pressed:
                                notLost = False
                                roundOver= True
                                break
                        xenoPrintOver("XENOBUZZ" + "\n")
                        if not notLost:
                            xenoPrint(
                                "Didn't press it in time. Game over. Planet doomed, civilisation over, etcetc u ruined everyone's life")
                            xenoPrint("You did get past " + str(counterL) + " enemies though")
                            break
                        counterL += 1
                        break
                elif counterL % 5 == 0:
                    key_pressed = False
                    wkey_pressed = False
                    roundOver = False
                    def detect_key_pressE():
                        global key_pressed
                        while not keyboard.is_pressed('e'):
                            pass
                        key_pressed = True

                    def detect_key_pressO():
                        global wkey_pressed
                        while not keyboard.is_pressed('q') and not keyboard.is_pressed('w') and not keyboard.is_pressed('s') and not roundOver:
                            pass
                        wkey_pressed = True

                    while True:
                        threadE = Thread(target=detect_key_pressE)
                        threadE.start()
                        threadO = Thread(target=detect_key_pressO)
                        threadO.start()
                        incrementSleep = (4 / (counterL ** (1 / 10))) / 10
                        for i in range(11):
                            xenoPrintOver('--' * (10-i))
                            time.sleep(incrementSleep)
                            if wkey_pressed:
                                notLost = False
                                break
                            elif key_pressed:
                                wkey_pressed = False
                                roundOver = True
                                break
                            elif i == 10 and not key_pressed:
                                notLost = False
                                roundOver = True
                                break
                        xenoPrintOver("BUZZ" + "\n")
                        if not notLost:
                            xenoPrint(
                                "Didn't press it in time. Game over. Planet doomed, civilisation over, etcetc u ruined everyone's life")
                            xenoPrint("You did get past " + str(counterL) + " enemies though")
                            break
                        counterL += 1
                        break
                elif counterL % 3 == 0:
                    key_pressed = False
                    wkey_pressed = False
                    roundOver = False

                    def detect_key_pressQ():
                        global key_pressed
                        while not keyboard.is_pressed('q'):
                            pass
                        key_pressed = True

                    def detect_key_pressO():
                        global wkey_pressed
                        while not keyboard.is_pressed('s') and not keyboard.is_pressed('w') and not keyboard.is_pressed('e') and not roundOver:
                            pass
                        wkey_pressed = True


                    while True:
                        threadQ = Thread(target=detect_key_pressQ)
                        threadQ.start()
                        threadO = Thread(target=detect_key_pressO)
                        threadO.start()
                        incrementSleep = (4 / (counterL ** (1 / 10))) / 10
                        for i in range(11):
                            xenoPrintOver('--' * (10-i))
                            time.sleep(incrementSleep)
                            if wkey_pressed:
                                notLost = False
                                break
                            elif key_pressed:
                                roundOver = True
                                wkey_pressed = False
                                break
                            elif i == 10 and not key_pressed:
                                notLost = False
                                roundOver= True
                                break
                        xenoPrintOver("XENO" + "\n")
                        if not notLost:
                            xenoPrint(
                                "Didn't press it in time. Game over. Planet doomed, civilisation over, etcetc u ruined everyone's life")
                            xenoPrint("You did get past " + str(counterL) + " enemies though")
                            break
                        counterL += 1
                        break
                else:
                    key_pressed = False
                    wkey_pressed = False
                    roundOver = False

                    def detect_key_pressS():
                        global key_pressed
                        while not keyboard.is_pressed('s'):
                            pass
                        key_pressed = True

                    def detect_key_pressO():
                        global wkey_pressed
                        while not keyboard.is_pressed('q') and not keyboard.is_pressed('w') and not keyboard.is_pressed('e') and not roundOver:
                            pass
                        wkey_pressed = True


                    while True:
                        threadS = Thread(target=detect_key_pressS)
                        threadS.start()
                        threadO = Thread(target=detect_key_pressO)
                        threadO.start()
                        incrementSleep = (4 / (counterL ** (1 / 10))) / 10
                        for i in range(11):
                            xenoPrintOver('--' * (10-i))
                            time.sleep(incrementSleep)
                            if wkey_pressed:
                                notLost = False
                                break
                            elif key_pressed:
                                roundOver = True
                                wkey_pressed = False
                                break
                            elif i == 10 and not key_pressed:
                                notLost = False
                                roundOver= True
                                break
                        xenoPrintOver(str(counterL) + "\n")
                        if not notLost:
                            xenoPrint("Didn't press it in time or pressed the wrong button. Game over. Planet doomed, civilisation over, etcetc u ruined everyone's life")
                            xenoPrint("You did get past " + str(counterL) + " enemies though")
                            break
                        counterL += 1
                        break
                time.sleep(0.5)
        elif menuInput.upper() == "F":
            xenoPrint("Game closing. Planet doomed, civilisation over, etcetc u ruined everyone's life")
            break
        else:
            xenoPrint("no clue what you just input, try again")






#  my personal favourite words to use are ronk and bonk
#  but the world is your oyster
#
# a̶l̶s̶o̶ ̶m̶y̶ ̶c̶o̶m̶m̶e̶n̶t̶s̶ ̶a̶r̶e̶ ̶k̶i̶n̶d̶a̶ ̶m̶e̶s̶s̶y̶ ̶t̶o̶ ̶b̶e̶ ̶r̶i̶g̶h̶t̶ ̶a̶f̶t̶e̶r̶ ̶e̶a̶c̶h̶
# l̶i̶n̶e̶ ̶i̶n̶s̶t̶e̶a̶d̶ ̶o̶f̶ ̶b̶e̶f̶o̶r̶e̶ ̶s̶o̶ ̶m̶a̶y̶b̶e̶ ̶t̶h̶a̶t̶ ̶c̶o̶u̶l̶d̶ ̶b̶e̶ ̶i̶m̶p̶r̶o̶v̶e̶d̶

