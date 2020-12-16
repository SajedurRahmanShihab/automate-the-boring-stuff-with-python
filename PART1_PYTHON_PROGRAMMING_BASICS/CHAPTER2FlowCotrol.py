# Boolean Values
import sys
import random
spam = True
print(spam)

# Comparison Operators
"""
==   Equal to
!=   Not equal to
<    Less than
>    Greater than
<=   Less than or equal to
>=   Greater than or equal to
"""


# Mixing Boolean and Comparison Operator
print((4 < 5) and (5 < 6))

# Blocks of Code
name = "Shihab"
password = "swordfish"
if name == "Shihab":
    print("Hello", "Shihab")
    if password == "swordfish":
        print("Access granted")
    else:
        print("Wrong password")


# while Loop Statement
spam = 0
if spam < 5:
    print("Hello, world")
    spam = spam + 1

# Here is the code with a while statement
spam = 0
while spam < 5:
    print("Hello, world.")
    spam = spam + 1


# An Annoying while Loop
"""name = ""
while name != "your name":
    print("Please type your name")
    name = input()
print("Thank You!")
"""
# break statement
"""while True:
    print("Please type your name.")
    name = input()
    if name == "your name":
        break
print("Thank You")
"""

# continue statements
"""while True:
    print("Who are you?")
    name = input()
    if name != "Joe":
        continue
    print("Hello, Joe. What is the password? (It is a fish)")
    password = input()
    if password == "swordfish":
        break
print("Access granted")
"""

# for Loops and the range() Function
total = 0
for num in range(101):
    total = total + num
print(total)

# An Equivalent while Loop
print("My name is")
i = 0
while i < 5:
    print("Jimmy Five Times (" + str(i) + ")")
    i = i + 1


# The Starting, Stopping, and Stepping Arguments to range()
for i in range(12, 16):
    print(i)

print("New Piece of code")

for i in range(0, 10, 2):
    print(i)

print("New Piece of code")

for i in range(5, -1, -1):
    print(i)

print("New Piece of code")
# Importing Modules
for i in range(5):
    print(random.randint(1, 10))

print("New Piece of code")

# Ending A Program Early with the SYS.EXIT() Function
"""while True:
    print("Type exit to exit.")
    response = input()
    if response == "exit":
        sys.exit()
    print("You typed " + response + ".")"""

print("New Piece of code")
# A Short Program: Guess the number
# This is a guess the number game.
secretNumber = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")

# Ask the player to guess 6 times
"""for guessTaken in range(1, 5):
    print("Take a guess: ")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break  # This condition is the correct the guess!

if guess == secretNumber:
    print("Great job! You guessed my number in " + str(guessTaken) + " guesses!")
else:
    print("Nope. The number I was thinking of was " + str(secretNumber))"""


print("New Piece of code")

# A Short Program: Rock, Paper, Scissors
print("ROCK, PAPER, SCISSORS")
# These variables keep of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True:  # The main game loop.
    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))
    while True:  # The player input loop.
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        playerMove = input()
        if playerMove == "q":
            sys.exit()  # Quit the program
        if playerMove == "r" or playerMove == "p" or playerMove == "s":
            break
        print("Type one of r, p, s or q.")

    # Display what the player chose:
    if playerMove == "r":
        print("ROCK versus.....")
    elif playerMove == "p":
        print("PAPER versus.....")
    elif playerMove == "s":
        print("SCISSORS versus.....")

    # Display what computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = "r"
        print("ROCK")
    elif randomNumber == 2:
        computerMove = "p"
        print("PAPER")
    elif randomNumber == 3:
        computerMove = "s"
        print("SCISSORS")

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print("It is a tie!")
        ties = ties + 1
    elif playerMove == "r" and computerMove == "s":
        print("You win!")
        wins = wins + 1
    elif playerMove == "p" and computerMove == "r":
        print("You win!")
        wins = wins + 1
    elif playerMove == "s" and computerMove == "p":
        print("You win!")
        wins = wins + 1
    elif playerMove == "r" and computerMove == "p":
        print("you lose!")
        losses = losses + 1
    elif playerMove == "p" and computerMove == "s":
        print("you lose!")
        losses = losses + 1
    elif playerMove == "s" and computerMove == "r":
        print("you lose!")
        losses = losses + 1


# PRACTICE QUESTION
"""
1. What are the two values of the Boolean data type? How do you write them?
Answer:
True
False

2. What are the three Boolean operators?
Answer:
and, or, not

3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).
Answer:
True True = True
True False = False
vice versa

4. What do the following expressions evaluate to?
Answer:
(5 > 4) and (3 == 5) False
not (5 > 4) False
(5 > 4) or (3 == 5) True
not ((5 > 4) or (3 == 5)) False
(True and True) and (True == False) False
(not False) or (not True) True

5. What are the six comparison operators?
Answer:
<, >, >=, <=, !=, ==

6. What is the difference between the equal to operator and the assignment operator?
Answer:
= this is an assign operator, which assing value into a variable
== this is an equal operator which is a comparision operator

7.  Explain what a condition is and where you would use one.
Answer: A condition defines whether a mathmetical expression is true of false. We can use it in many different circumstances, such as iteration, if else statement and so on so forth

8. Identify the three blocks in this code:
spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')

9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
Answer:
spam = 1
if spam == 1 :
    print("Hello")
elif spam == 2:
    print("Howdy")
else: 
    print("Greetings!")

10. What keys can you press if your program is stuck in an infinite loop?
Answer:
CLT + C

11. What is the difference between break and continue?
Answer:
Break leaves the loop completely and executes the statements after the loop. Whereas Continue leaves the current iteration and executes with the next value in the loop.

12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
Answer:
ranger(10) 0-9
range(0,10) 0-9
range(0, 10, 1) 0-9
no difference

13. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
Answer;
for i in range(1, 11):
    print(i)

i = 1
while i < 11:
    print(i)
    i = i + 1


14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
Answer:
import spam
spam.bacon()

"""
