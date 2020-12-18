# Dictionaries And Structuring Data
# The dictionary data type

import pprint
myCat = {"size": "fat", "color": "gray", "disposition": "loud"}
print(myCat["size"])

# Dictionaries vs. Lists
spam = ["cats", "dogs", "moose"]
bacon = ["dogs", "moose", "cats"]
print(spam == bacon)

eggs = {"name": "Zophie", "species": "cat", "age": "8"}
ham = {"species": "cat", "age": "8", "name": "Zophie"}
print(eggs == ham)

# Birthday
birthdays = {"Alice": "Apr 1", "Bob": "Dec 12", "Carol": "Mar 4"}
while True:
    print("Enter a name:(blank to quit)")
    name = input()
    if name == "":
        break

    if name in birthdays:
        print(birthdays[name] + " is the birthday of "+name)
    else:
        print("I do not have birthday information for " + name)
        print("What is their birthday?")
        bday = input()
        birthdays[name] = bday
        print("Birthday database updated.")


# The keys(), values(), and items() Methods
spam = {"color": "red", "age": 42}
for v in spam.values():
    print(v)

for k in spam.keys():
    print(k)

print(spam.keys())

for k, v in spam.items():
    print("Key: " + k + " Value: "+str(v))


# Checking Whether a Key or Value Exists in a Dictionary
spam = {"name": "Zophie", "age": 7}
print("name" in spam.keys())


# The get() Method
picnicItems = {"apples": 5, "cups": 2}
print("I am bringing " + str(picnicItems.get('cups', 0)) + ' cups')

# The setdefault() Method
# spam = {"name": "Pooka", "age": 5}
# if "color" not in spam:
#     spam["color"] = "black"

print(spam.setdefault("color", "black"))
print(spam)


# short program that counts the number of occurrences of each letter in a string
message = "It was a bright cold day in April, and the clocks were striking thirteen."
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)


# Pretty Printing
message = "It was a bright cold day in April, and the clocks were striking thirteen."
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)


# A Tic-Tac-Toe Board
theBoard = {"top-L": " ", "top-M": " ", "top-R": " ",
            "mid-L": " ", "mid-L": " ", "mid-R": " ", "low-L": " ", "low-M": " ", "low-R": " "
            }


def printBoard(board):
    print(board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
    print("-+-+-")
    print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
    print("-+-+-")
    print(board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"])


turn = "X"

for i in range(9):
    printBoard(theBoard)
    print("Turn for " + turn + ".Move on which space?")
    move = input()
    theBoard[move] = turn
    if turn == "X":
        turn = "0"
    else:
        turn = "X"


# Nested Dictionaries and Lists
allGuests = {"Alice": {"apples": 5, "pretzels": 12}, "Bob": {
    "ham sandwiches": 3, "apples": 2}, "Carol": {"Cups": 3, "Apple pies": 1}}


def totalBrought(guests, item):
    numBought = 0
    for k, v in guests.items():
        numBought = numBought + v.get(item, 0)
    return numBought


print("Number of things being brought")
print("-Apples   "+str(totalBrought(allGuests, "apples")))


# Practice Question
"""
1. What does the code for an empty dictionary look like?
Ans:
myDict = {}

2. What does a dictionary value with a key 'foo' and a value 42 look like?
Ans:
myDict = {
    "foo" : 42
}

3. What is the main difference between a dictionary and a list?
Ans:
list allows duplicate item, dictionary don't

4. What is the main difference between a dictionary and a list?
Ans:
Raise an error

5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
Ans:
cat returns whether the "cat" key available in the dictionary, and spam.values() return all the value in the dictionary

6. What  is the shortcut for the following code?
if "color" not in spam:
    spam["color"] = "black"
Ans:
spam.setdefault("color", "black")

7. What module and function can be used to "pretty" dictionary values?
Ans:
Module : pprint
Function : pprint
"""
