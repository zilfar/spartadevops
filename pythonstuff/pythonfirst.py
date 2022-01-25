# Complete = False
#
# while not Complete:
#     print("I'd like to know your name, age and your favourite colour!\n")
#     firstAnswer = input("Please tell me your name, first of all.\n")
#     if firstAnswer.isalpha():
#         print("That's a nice name!")
#         secondAnswer = input("Could you tell me your age now, please? Only numbers now :)\n")
#         if not secondAnswer.isalpha() and 120 > int(secondAnswer) >= 0:
#             print("Great!")
#             finalAnswer = input("This is the final question, what is your favourite colour?\n")
#             if finalAnswer.isalpha():
#                 print("Fantastic!\n")
#                 print("So, your name is " + firstAnswer.capitalize() + ", you're " + secondAnswer + " years old and your favourite colour is " + finalAnswer + "! Nice to meet you :)")
#                 Complete = True
#             else:
#                 print("Your favourite colour can't be a number! Use your words! Let's start over.\n\n")
#         else:
#             print("Either your answer is ridiculous or wasn't numeric. Let's start from scratch.\n")
#     else:
#         print("please try again. Names have only alphabetic letters in them!\n")
#
#
# prompt_user = True
# age = None
# while prompt_user:
#     age = input("What is your age?\n")
#     if age.isdigit():
#
#         if int(age) == 0:
#             print(f"Double your age is {int(age) * 2} ... You're zero years old? Try again.")
#         if 0 < int(age) < 18:
#             print(f"Double your age is {int(age) * 2} ... that means you're a little bit young.")
#             prompt_user = False
#         elif int(age) < 100:
#             print(f"Double your age is {int(age) * 2}")
#             prompt_user = False
#         elif int(age) < 120:
#             print(f"Double your age is {int(age) * 2} ... A ripe old age.")
#             prompt_user = False
#         elif int(age) >= 120:
#             print(f"Double your age is {int(age) * 2} ... Maybe a bit too old. Try again.")
#
#     else:
#         print("Please provide a sensible age in digits.")
#
print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a:
for number in x[:5]:
    print(number)


print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:
for number in x:
    if number % 2 == 0:
        print(number)


print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:
for number in x[:5]:
    if number % 2 == 0:
        print(number)

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]

# A2a:
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

newList = []
for name in names:
    newList.append(name[0])
print(newList)



print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:
newList = []
for name in names:
    newList.append(name.index(' '))
print(newList)



print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual

# A2c:
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]
newList = []
for name in names:
    newList.append(name[0] + name.split(" ")[1][0])
print(newList)

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
 list_of_lists = [[1,5,7,3,44,4,1],
                  ["A", "B", "C"],
                  ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                  ["one", "Two", "Three", "Four"]]
#
#
# # A3a:
for lists in list_of_lists:
    if len(lists) == len(set(lists)):
        print(lists)




# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:
while True:
    numberInput = input("enter an integer greater than 100\n")
    if numberInput.replace(".", "", 1).isdigit() and float(numberInput) > 100:
        print(str(float(numberInput)))
        break
    else:
        print("try again")



print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:
while True:
    numberInput = input("enter an integer greater than 100\n")
    if numberInput.replace(".", "", 1).isdigit() and float(numberInput) > 100:
        print(str(float(numberInput)))
        factorCounter = 0
        if "." not in numberInput:
            for x in range(1,int(numberInput)+1):
                if int(numberInput) % x == 0:
                    factorCounter += 1
            if factorCounter == 2:
                print("this is a prime n5umber!")
        elif not factorCounter == 2:
            print("this is not a prime number")
        break
    else:
        print("try again")

print("\nQ1a\n")


# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:
def f(integer: int):
    list_of_factors = []
    for factor in range(1, int(integer) + 1):
        if int(integer) % factor == 0:
            list_of_factors.append(factor)
    return list_of_factors


print("\nQ1b\n")


# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:
def isFactorOf(int1: int, int2: int):
    if int1 in f(int2):
        return True
    else:
        return False


# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]


# A2a:
def alphabetPosition(letter: str):
    return alphabet.index(letter)


print("\nQ2b\n")


# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:

def idName(name: str):
    id = ""
    for letter in name:
        id += str(alphabetPosition(letter))
    return id


print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:

def idToPassword(id: str):
    sum = 0
    for char in id:
        sum += int(char)
    return str(int(id) - sum)

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")


# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:


def isPrime(int1: int):
    if len(f(int1)) == 2:
        return True
    else:
        return False


print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:

def isPrime(int1):
    if int1.isdigit():
        if len(f(int1)) == 2:
            return True
        else:
            return False


# -------------------------------------------------------------------------------------- #

#
# def add(int1: int, int2: int) -> int:
#     return int(int1) + int(int2)
#
#
# def subtract(int1: int, int2: int) -> int:
#     return int(int1) - int(int2)
#
#
# def multiply(int1: int, int2: int) -> int:
#     return int(int1) * int(int2)
#
#
# def divide(int1: int, int2: int) -> float:
#     return int(int1) / int(int2)