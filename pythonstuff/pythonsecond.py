noInput = True # have boolean that i can change to break out of while loop

# keep looping if i haven't changed my boolean yet
while noInput:

    # ask user to put in a final number to play fizzbuzz to
    rangeF = input("up to what number would you like to play fizzbuzz to\n")

    # make sure user input is an integer which is larger than 0
    if rangeF.isnumeric() and int(rangeF) > 0:

        # ask user for first word to use instead of fizz
        firstWord = input('next, add an alternative word for \'fizz\', leave it empty to keep fizz.\n')

        # check if the length of the word (after stripping whitespace) is at least 1 char, and check if it's only
        # using alphabetical chars
        if len(firstWord.strip()) < 1 or not firstWord.isalpha():

            # if they violate the rules they don't deserve to have their own word
            print('seems dodgy so i\'m just using fizz for the first word')
            # so we use fizz as the default
            firstWord = 'fizz'

        # ask user for second word to use instead of buzz
        secondWord = input('next, add a second alternative word for \'buzz\', leave it empty to keep buzz.\n')

        # check if the length of the word (after stripping whitespace) is at least 1 char, and check if it's only
        # using alphabetical chars
        if len(secondWord.strip()) < 1 or not secondWord.isalpha():

            # if they violate the rules they don't deserve to have their own word
            print('seems dodgy so i\'m just using buzz for the first word')
            # so we use buzz as the default
            firstWord = 'buzz'

        # after everything is done, all the variables have a right value we can change this boolean to break out of
        # the while loop and continue onto our game
        noInput = False

    # oh and if they give a bad answer for the range then just make them try again
    else:
        # at least you get to try again this time instead of having a default value
        print('you gave a weird response idk try again')

# iterate over a loop that contains numbers from 1 up to the input number (+1 because end range isn't inclusive!!!)
for x in range(1, int(rangeF)+1):

    # if they're a factor of 3 and 5 then by simplification they're also a factor of 15, makes it easier to write,
    # so we bring out the fizzbuzz
    if x % 15 == 0: print(firstWord + secondWord)

    # otherwise, check if it's at least a factor of 3, then bring out the fizz
    elif x % 3 == 0: print(firstWord)

    # if not then it could be a factor of 5, which brings out the buzz
    elif x % 5 == 0: print(secondWord)

    # otherwise just print the normal number down since they don't fit into the 3 and 5s
    else: print(x)


#  my personal favourite words to use are ronk and bonk
#  but the world is your oyster
#
# a̶l̶s̶o̶ ̶m̶y̶ ̶c̶o̶m̶m̶e̶n̶t̶s̶ ̶a̶r̶e̶ ̶k̶i̶n̶d̶a̶ ̶m̶e̶s̶s̶y̶ ̶t̶o̶ ̶b̶e̶ ̶r̶i̶g̶h̶t̶ ̶a̶f̶t̶e̶r̶ ̶e̶a̶c̶h̶
# l̶i̶n̶e̶ ̶i̶n̶s̶t̶e̶a̶d̶ ̶o̶f̶ ̶b̶e̶f̶o̶r̶e̶ ̶s̶o̶ ̶m̶a̶y̶b̶e̶ ̶t̶h̶a̶t̶ ̶c̶o̶u̶l̶d̶ ̶b̶e̶ ̶i̶m̶p̶r̶o̶v̶e̶d̶
