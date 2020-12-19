spam = "This is Alice's cat."

# Escape Chracters
spam = "Say hi to Bob\'s mother."
print(spam)

"""Escape character  Print as
\'                Single quote
\"                Double quote
\t                Tab
\n                Newline (line break)
\\                Backslash"""

print("Hello there!\nHow are you?\nI\'m doing fine.")


# Raw String
print(r"That is Carol\'s cat.")


# Multiple Strings with Triple Quotes
print("""
Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion

Sincerely,
Bob

""")


# Indexing and Slicing Strings
spam = "Hello, world!"
print(spam[0])

# The in and not Operators with Strings
foo = "Hello, World!"
print("Hello" in foo)
print("!" not in foo)

# Puting Strings Inside Other Strings
name = "AI"
age = 4000
print("Hello, my name is " + name + " I am " + str(age) + " years old.")


# Better way
print("My name is %s. I am %s years old." % (name, age))

# f-strings
print(f"My name is {name}. Next year I will be {age + 1}.")

# Useful String Method
# The upper(), lower(), isupper(), and islower() methods
spam = "Hello, world!"
print(spam.upper())
print(spam.lower())

print("How are you?")
feeling = input()
if feeling.lower() == "great":
    print("I feel great too")
else:
    print("I hope the rest of your day is good")


# isupper() and islower()
spam = "Hello, world"
print(spam.islower())

# The isX() Method()
# Returns True if the string consists only of letters and isn’t blank
print("Hello ".isalpha())

# Returns True if the string consists only of letters and numbers and is not blank
print("Hello".isalnum())

# Returns True if the string consists only of spaces, tabs, and newlines and is not
print(" ".isspace())

# Returns True if the string consists only of numeric characters and is not blank
print("11234".isdecimal())

# Returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters
print("This Is Title Case".istitle())

# The isX() string methods are helpful when you need to validate user input.
while True:
    print("Enter your age: ")
    age = input()
    if age.isdecimal():
        break
    print("Please enter a number for your age.")

while True:
    print("Select a new password (letters and numbers only): ")
    password = input()
    if password.isalnum():
        break
    print("Password can only have letterss and numbers.")


# The startswith() and endswith() Methods
print("Hello, world!".startswith("Hello"))
print('Hello, world!'.endswith('Hello, world!'))


# The join() and split() Methods
print(",".join(["cat", "rats", "bats"]))

print("My name is Simon".split())
print("MyABCnameABCisABCSimon".split("ABC"))

spam = """Dear Alice,
How have you been? I am fine.
There is aa container in the fridge
that is labeled "Milk Experiment."

Please do not drink it.
Sincerely,
Bob
"""
print(spam.split("\n"))


# Splitting String with the partition() Method
# The partition() string method can split a string into the text before and after a separator string
print("Hello, world!".partition("w"))
before, sep, after = "Hello, world!".partition(" ")
print(before, sep, after)


# Justifying Text with the rjust(), ljust(), and center() Methods
print("Hello".rjust(10))
print("Hello".ljust(20))
print("Hello".rjust(20, "*"))
print("Hello".center(20))
print("Hello".center(20, "="))


def printPicnic(itemsDict, leftWidth, rightWidth):
    print("PICNIC ITEMS".center(leftWidth + rightWidth, "-"))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, ".") + str(v).rjust(rightWidth))


picnicItems = {"sandwiches": 4, "apples": 12, "cups": 4, "cookies": 8000}
printPicnic(picnicItems, 12, 5)

# Removing Whitespace with strip(), rstrip(), and lstrip() Methods
spam = " Hello, World "
print(spam.strip())
print(spam.rstrip())
print(spam.lstrip())


# Numeric Values of Characters with the ord() and chr() function
print(ord('A'))
print(ord("4"))


# Copying and Pasting Strings with the Pyperclip Module


# Practice Question
"""1. What are escape characters?
Ans:
which escape the sequence

2. What do the \n and \t escape characters represent?
Ans:
new line and tab

3. How can you put a \ backslash character in a string?
Ans:
By putting \\

4. The string value "Howl's Moving Castle" is a valid string. Why isn’t it a problem that the single quote character in the word Howl's isn’t escaped?
Ans:
Because it start and ended with double quote

5.  If you don’t want to put \n in your string, how can you write a string with newlines in it?
Starting and ending with """

6. What do the following expressions evaluate to?

'Hello, world!'[1]   e
'Hello, world!'[0:5]  Hello
'Hello, world!'[:5]  Hello
'Hello, world!'[3:] lo, world!

7.  What do the following expressions evaluate to?
'Hello'.upper()  "HELLO"
'Hello'.upper().isupper() True
'Hello'.upper().lower() "hello"
"""
