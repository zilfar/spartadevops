noInput = True  # have boolean that i can change to break out of while loop
theGame = False  # super secret high technology variable (don't look into it if you value your life)

# define a few actions that we'll use often in xenobuzz
XENO = "---------------------------------------- "


def xenoPrint(string):

    print(XENO + string)


def xenoInput(string):
    return input(XENO + string + "\n" + XENO)


def xenoPrintOver(string):
    sys.stdout.write('\r' + XENO + string)


def xenoNL():
    print(XENO)

# visual clarity
print("\n")

while True:
    xenoPrint("a secret experimental version of fizzbuzz has escaped area 51 ")
    xenoPrint("and we're looking for patients brave enough to try and figure it out")
    yesorno = xenoInput('are you up to the task? Y/N').strip()
    if yesorno.upper() == "Y":
        xenoPrint("you have entered the xenobuzz".upper())
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
        if x % 15 == 0:
            print("waaa")

        # otherwise, check if it's at least a factor of 3, then bring out the fizz
        elif x % 3 == 0:
            print(firstWord)

        # if not then it could be a factor of 5, which brings out the buzz
        elif x % 5 == 0:
            print(secondWord)

        # otherwise just print the normal number down since they don't fit into the 3 and 5s
        else:
            print(x)
# xenobuzz begins
else:
    # import modules only when needed to prevent slow load times
    import time
    import keyboard
    import sys
    from threading import Thread
    xenoPrint("The Xenobuzz attacks in multiples of 3 and 5".upper())
    xenoPrint("You must hold back the Xenobuzz infiltration. You are the last line of defense and"
              " if you don't block them in time you will doom the planet yada yada".upper())
    # while loop to stay in the menu until game is exited
    while True:
        xenoNL()

        # ask user for menu action
        menuInput = xenoInput("Enter 'C' for controls, 'S' to start the game and 'F' to exit the game.".upper())

        # print controls
        if menuInput.upper() == "C":
            xenoNL()
            xenoPrint('Once the game begins, you have to press buttons in accordance with'
                      ' whether they will be a regular enemy ("S"),'.upper())
            xenoPrint('a xeno enemy which is a multiple of 3 ("Q"), a buzz enemy which is a multiple'
                      ' of 5 ("E") or the dreaded xenobuzz which is a multiple of both 3 and 5 ("W")'.upper())
            xenoPrint('however, the xenobuzz are feared mainly because of how fast their'
                      ' attacks ramp up, and it could get overwhelming really quickly.'.upper())
            xenoNL()
            xenoPrint("W: Multiple of 3 AND 5")
            xenoPrint("E: Multiple of 5")
            xenoPrint("Q: Multiple of 3")
            xenoPrint("S: Everything else")

        # begin game
        elif menuInput.upper() == "S":
            counterL = 1
            notLost = True

            # stay in game until it is lost
            while notLost:

                # xenobuzz
                if counterL % 15 == 0:
                    key_pressed = False
                    wkey_pressed = False
                    roundOver = False

                    # two functions to detect keypresses, one for the
                    # right keypress and one for the incorrect keypresses
                    def detect_key_pressW():
                        global key_pressed
                        while not keyboard.is_pressed('w'):
                            pass
                        key_pressed = True


                    def detect_key_pressO():
                        global wkey_pressed
                        while not keyboard.is_pressed('q') \
                                and not keyboard.is_pressed('s') and not keyboard.is_pressed('e') and not roundOver:
                            pass
                        wkey_pressed = True


                    while True:
                        # begin the asynchronous threads to track keyboard presses while executing code
                        threadW = Thread(target=detect_key_pressW)
                        threadW.start()
                        threadO = Thread(target=detect_key_pressO)
                        threadO.start()

                        # sleep in the total sleep time divided by 10, where the total sleep time is calculated
                        # using the inverse of the current number to the power of 1/7 (so it speeds up fast to
                        # begin with, and decelerates as you go on)
                        incrementSleep = (2.5 / (counterL ** (1 / 7))) / 10
                        for i in range(11):
                            xenoPrintOver('--' * (10-i))
                            time.sleep(incrementSleep)

                            # if the wrong key is pressed
                            if wkey_pressed:
                                notLost = False
                                break

                            # if the right key is pressed
                            elif key_pressed:
                                wkey_pressed = False
                                roundOver = True
                                break

                            # if they key isn't pressed, check if the time is over
                            elif i == 10 and not key_pressed:
                                notLost = False
                                roundOver = True
                                break
                        xenoPrintOver("XENOBUZZ" + "\n")

                        # game lost
                        if not notLost:
                            xenoPrint(
                                "Didn't press it in time or pressed the wrong button. Game over."
                                " Planet doomed, civilisation over, etcetc u ruined everyone's life".upper())
                            xenoPrint("You did get past ".upper() + str(counterL) + " enemies though".upper())
                            break

                        # increase counter of counterL by 1 to progress the game
                        counterL += 1
                        break

                # buzz
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
                        while not keyboard.is_pressed('q')\
                                and not keyboard.is_pressed('w') and not keyboard.is_pressed('s') and not roundOver:
                            pass
                        wkey_pressed = True

                    while True:
                        threadE = Thread(target=detect_key_pressE)
                        threadE.start()
                        threadO = Thread(target=detect_key_pressO)
                        threadO.start()
                        incrementSleep = (2.5 / (counterL ** (1 / 7))) / 10
                        for i in range(11):
                            xenoPrintOver('--' * (10 - i))
                            time.sleep(incrementSleep)

                            # if the wrong key is pressed
                            if wkey_pressed:
                                notLost = False
                                break

                            # if the right key is pressed
                            elif key_pressed:
                                wkey_pressed = False
                                roundOver = True
                                break

                            # if they key isn't pressed, check if the time is over
                            elif i == 10 and not key_pressed:
                                notLost = False
                                roundOver = True
                                break
                        xenoPrintOver("BUZZ" + "\n")

                        # game lost
                        if not notLost:
                            xenoPrint(
                                "Didn't press it in time or pressed the wrong button."
                                " Game over. Planet doomed, civilisation over, etcetc u ruined everyone's life".upper())
                            xenoPrint("You did get past ".upper() + str(counterL) + " enemies though".upper())
                            break

                        # increase counter of counterL by 1 to progress the game
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
                        while not keyboard.is_pressed('s')\
                                and not keyboard.is_pressed('w') and not keyboard.is_pressed('e') and not roundOver:
                            pass
                        wkey_pressed = True


                    while True:
                        threadQ = Thread(target=detect_key_pressQ)
                        threadQ.start()
                        threadO = Thread(target=detect_key_pressO)
                        threadO.start()
                        incrementSleep = (2.5 / (counterL ** (1 / 7))) / 10
                        for i in range(11):
                            xenoPrintOver('--' * (10 - i))
                            time.sleep(incrementSleep)

                            # if the wrong key is pressed
                            if wkey_pressed:
                                notLost = False
                                break

                            # if the right key is pressed
                            elif key_pressed:
                                wkey_pressed = False
                                roundOver = True
                                break

                            # if they key isn't pressed, check if the time is over
                            elif i == 10 and not key_pressed:
                                notLost = False
                                roundOver = True
                                break
                        xenoPrintOver("XENO" + "\n")

                        # game lost
                        if not notLost:
                            xenoPrint(
                                "Didn't press it in time or pressed the wrong button."
                                " Game over. Planet doomed, civilisation over, etcetc u ruined everyone's life".upper())
                            xenoPrint("You did get past ".upper() + str(counterL) + " enemies though".upper())
                            break

                        # increase counter of counterL by 1 to progress the game
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
                        while not keyboard.is_pressed('q')\
                                and not keyboard.is_pressed('w') and not keyboard.is_pressed('e') and not roundOver:
                            pass
                        wkey_pressed = True


                    while True:
                        threadS = Thread(target=detect_key_pressS)
                        threadS.start()
                        threadO = Thread(target=detect_key_pressO)
                        threadO.start()
                        incrementSleep = (2 / (counterL ** (1 / 5))) / 10
                        for i in range(11):
                            xenoPrintOver('--' * (10 - i))
                            time.sleep(incrementSleep)

                            # if the wrong key is pressed
                            if wkey_pressed:
                                notLost = False
                                break

                            # if the right key is pressed
                            elif key_pressed:
                                wkey_pressed = False
                                roundOver = True
                                break

                            # if they key isn't pressed, check if the time is over
                            elif i == 10 and not key_pressed:
                                notLost = False
                                roundOver = True
                                break
                        xenoPrintOver(str(counterL) + "\n")

                        # game lost
                        if not notLost:
                            xenoPrint("Didn't press it in time or pressed the wrong button. Game over."
                                      " Planet doomed, civilisation over, etcetc u ruined everyone's life".upper())
                            xenoPrint("You did get past ".upper() + str(counterL) + " enemies though".upper())
                            break

                        # increase counter of counterL by 1 to progress the game
                        counterL += 1
                        break
                xenoPrintOver("")
                time.sleep(0.5)

        # press F to close the game
        elif menuInput.upper() == "F":
            xenoPrint("Game closing. Planet doomed, civilisation over, etcetc u ruined everyone's life".upper())
            break

        # otherwise, incorrect input
        else:
            xenoPrint("no clue what you just input, try again".upper())


#  my personal favourite words to use are ronk and bonk
#  but the world is your oyster
#  also my highscore on xenobuzz was only 36, try to beat my score maybe
#  my highscore is now 41
#  a̶l̶s̶o̶ ̶m̶y̶ ̶c̶o̶m̶m̶e̶n̶t̶s̶ ̶a̶r̶e̶ ̶k̶i̶n̶d̶a̶ ̶m̶e̶s̶s̶y̶ ̶t̶o̶ ̶b̶e̶ ̶r̶i̶g̶h̶t̶ ̶a̶f̶t̶e̶r̶ ̶e̶a̶c̶h̶
#  l̶i̶n̶e̶ ̶i̶n̶s̶t̶e̶a̶d̶ ̶o̶f̶ ̶b̶e̶f̶o̶r̶e̶ ̶s̶o̶ ̶m̶a̶y̶b̶e̶ ̶t̶h̶a̶t̶ ̶c̶o̶u̶l̶d̶ ̶b̶e̶ ̶i̶m̶p̶r̶o̶v̶e̶d̶
#  nvm my comments suck again for the xenobuzz gamemode
#  ok the comments kinda improved
