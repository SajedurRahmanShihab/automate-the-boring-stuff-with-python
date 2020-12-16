# Operators
print("This is the operation of an EXPONENT operator", 2**3)
print("This is the operation of a MODULAS/REMAINDER operator", 22 % 8)
print("This the operation of an INTEGER DIVISION/FLOORED DIVISION operator", 22//8)
print("This the operation of an DIVISION operator", 22/8)
print("This the operation of an MULTIPLICATION operator", 3*5)
print("This the operation of an SUBTRACTION operator", 5-2)
print("This the operation of an ADDITION operator", 2+2)


# String Concatenation and Replication
print("Alice" + "Bob")
print("Alice " * 5)

# Storing Values in Variables
spam = 40
print(spam)
eggs = 2
print(spam + eggs)
print(spam + eggs + spam)
spam = spam + 2
print(spam)


# Your First Program
# This program says hello and asks for my name
print("HEllo, world!")
print("What is your name?")
myName = input()
print("It is good to meet you, ", myName)
print("The length of your name is: ", len(myName))
print("What is your age?")  # ask for their age
myAge = input()
print("You will be " + str(int(myAge)+1) + " in a year")

# Practice Questions
""" 
1. Questions: Which of the following are operators, and which are values?
Answer:
* = Operator
'hello' = values
-88.8 = values
- = operator
/ = operator
+ = operator
5 = value

2. Questions: Which of the following is a variable, and which is a string?
Answer:
spam = variable
'spam' = string

3. Questions: Name three data types
Answer:
integer, float, string

4. Questions: What is an expression made up of? What do all expressions do?
Answer:
Expressions are made up of operators, they always evaluate down to a single value.

5. Question: This chapter introduced assignment statements, like spam = 10. What is the difference between an expression and a statement?
Answer: Expressions are made up of operators but statement itself an operator, such as spam = 10, here "=" is a statement

6. What does the variable bacon contain after the following code runs?
bacon = 20
bacon + 1
Answer:
20

7. What should the following two expressions evaluate to?
'spam' + 'spamspam'
'spam' * 3
Answer:
spamspamspam
spamspamspam

8. Why is eggs a valid variable name while 100 is invalid?
Ans: 
Because "eggs" start with a string but 100 start with number

9. What three functions can be used to get the integer, floating-point number, or string version of a value?
Ans:
int(), float(), str()

10. Why does this expression cause an error? How can you fix it?
'I have eaten ' + 99 + ' burritos.'
Ans:
Python interpreter can't concatenate string and integer value. So "I have eaten " + str(99) + " burritos."


"""
