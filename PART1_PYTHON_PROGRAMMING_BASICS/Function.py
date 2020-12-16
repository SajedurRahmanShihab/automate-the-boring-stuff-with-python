import sys
import time
import random
# Return values and return statement


def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is certain"
    elif answerNumber == 2:
        return "It is decidedly so"
    elif answerNumber == 3:
        return "Yes"
    elif answerNumber == 4:
        return "Reply hazy try again"
    elif answerNumber == 5:
        return "Ask again later"
    elif answerNumber == 6:
        return "Concentrate and ask again"
    elif answerNumber == 7:
        return "My reply is no"
    elif answerNumber == 8:
        return "Outlook not so good"
    elif answerNumber == 9:
        return "Very doubtful"


r = random.randint(1, 9)
fortune = getAnswer(r)
# print(fortune)


# The Call Stack
def a():
    print("a() starts")
    b()
    d()
    print("a() returns")


def b():
    print("b() starts")
    c()
    print("b() returns")


def c():
    print("c() starts")
    print("c() returns")


def d():
    print("d() starts")
    print("d() returns")


a()

# Local and Global Scope
# def spam():
#     eggs = 31337
# spam()

# Exception Handling


def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print("Error Invalid argument")


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))


# Another way
def spam1(divideBy):
    return 42/divideBy


try:
    print(spam1(2))
    print(spam1(12))
    print(spam1(0))
    print(spam1(1))
except ZeroDivisionError:
    print("Error: Invalid argument")


# A Short Program: Zigzag
indent = 0
increaseIndent = True

try:
    while True:
        print(" " * indent, end="")
        print("*********")
        time.sleep(0.1)  # pause for 1/10 of a second

        if increaseIndent:
            indent = indent + 1
            if indent == 20:
                increaseIndent = False
        else:
            indent = indent - 1
            if indent == 0:
                increaseIndent = True
except KeyboardInterrupt:
    sys.exit()


# Practice Project
# The Collatz Sequence
def collatz(number):
    if number % 2 == 0:
        print(number//2)
        return number//2
    if number % 2 != 0:
        print(3*(number + 1))
        return (3*(number + 1))


try:
    while True:
        userInput = int(input())
        result = collatz(userInput)
        if result == 1:
            sys.exit()
except:
    print("You must enter an integer")
