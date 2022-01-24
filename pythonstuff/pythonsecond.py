noInput = True #have boolean that i can change to break out of while loop

while noInput: #keep looping if i haven't changed my boolean yet
    rangeF = input("up to what number would you like to play fizzbuzz to\n") #ask user to put in a final number to play fizzbuzz to
    if rangeF.isnumeric() and int(rangeF) > 0: #make sure user input is an integer which is larger than 0
        firstWord = input('next, add an alternative word for \'fizz\', leave it empty to keep fizz.\n') #ask user for first word to use instead of fizz
        if len(firstWord.strip()) < 1 or not firstWord.isalpha(): #check if the length of the word (after stripping whitespace) is at least 1 char, and check if it's only using alphabetical chars
            print('seems dodgy so i\'m just using fizz for the first word') #if they violate the rules they don't deserve to have their own word
            firstWord = 'fizz' #so we use fizz as the default
        secondWord = input('next, add a second alternative word for \'buzz\', leave it empty to keep buzz.\n') #ask user for first word to use instead of buzz
        if len(secondWord.strip()) < 1 or not secondWord.isalpha(): #check if the length of the word (after stripping whitespace) is at least 1 char, and check if it's only using alphabetical chars
            print('seems dodgy so i\'m just using buzz for the first word') #if they violate the rules they don't deserve to have their own word
            firstWord = 'buzz' #so we use buzz as the default
        noInput = False #after everything is done, all the variables have a right value we can change this boolean to break out of the while loop and continue onto our game
    else: #oh and if they give a bad answer for the range then just make them try again
        print('you gave a weird response idk try again') #at least you get to try again this time instead of having a default value

for x in range(1, int(rangeF)+1): #iterate over a loop that contains numbers from 1 up to the input number (+1 because end range isn't inclusive!!!)
    if x % 15 == 0: print(firstWord + secondWord) #if they're a factor of 3 and 5 then by simplification they're also a factor of 15, makes it easier to write, so we bring out the fizzbuzz
    elif x % 3 == 0: print(firstWord) #otherwise, check if it's at least a factor of 3, then bring out the fizz
    elif x % 5 == 0: print(secondWord) #if not then it could be a factor of 5, which brings out the buzz
    else: print(x) #otherwise just print the normal number down since they don't fit into the 3 and 5s

# my personal favourite words to use are ronk and bonk
# but the world is your oyster

#also my comments are kinda messy to be right after each line instead of before them so maybe that could be improved