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

