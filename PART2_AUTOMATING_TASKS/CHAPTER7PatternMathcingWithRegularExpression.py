# Finding Patterns Of text Without Regular Expression
import re
import math


def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != "-":
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print("Phone number found: " + chunk)

print("Done")


# Finding Patterns OF Text With Regular Expression
# Creating Regex Objects
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print("Phone number found: "+mo.group())


# If you want to detect these characters as part of your text pattern, you need to escape them with a backslash:If you want to detect these characters as part of your text pattern, you need to escape them with a backslash:

phoneNumRegex = re.compile(r"(\(\d\d\d\))(\d\d\d-\d\d\d\d)")
mo = phoneNumRegex.search("My phone number is (415)555-4242.")
print(mo.group(1))


# Matching Multiple Groups with the Pipe
# When both Batman and Tina Fey occur in the searched string, the first occurrence of matching text will be returned as the Match object
heroRegex = re.compile(r"Batman|Tina Fey")
mo1 = heroRegex.search("Batman and Tina Fey")
print(mo1.group())

mo2 = heroRegex.search("Tina Fey and Batman")
print(mo2.group())

batRegex = re.compile(r"Bat(man|mobile|copter|bat)")
mo = batRegex.search("Batmobile lost a wheel")
print(mo.group())

# Match zero or one of the group preceding this question mark.
phoneNumRegex = re.compile(r"(\d\d\d-)?\d\d\d-\d\d\d\d")
mol = phoneNumRegex.search("My number is 415-555-4242")
print(mol.group())


# Matching Zero or More with the Star
batRegex = re.compile(r"Bat(wo)*man")
mol = batRegex.search("The Adventures of Batman")
print(mol.group())
mo2 = batRegex.search("The adventures of Batwoman")
print(mo2.group())


# Matching One or More with the plus
batRegex = re.compile(r"Bat(wo)+man")
mol = batRegex.search("The Adventures of Batwoman")
print(mol.group())

mo2 = batRegex.search("The Adventures of Batman")
print(mo2 == None)


# Matching Specific Repetitions with Braces
haRegex = re.compile(r"(Ha){3}")
mol = haRegex.search("HaHaHa")
print(mol.group())


# Greedy and NON-GREEDY Mathing
# Python’s regular expressions are greedy by default
greedyHaRegex = re.compile(r"(Ha){3,5}")
mol = greedyHaRegex.search("HaHaHaHaHa")
print("Greedy Output")
print(mol.group())

nongreedyHaRegex = re.compile(r"(Ha){3,5}?")
mo2 = nongreedyHaRegex.search("HaHaHaHaHa")
print("Non greedy Output")
print(mo2.group())

# The FINDALL() Method
phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
# Output: ['415-555-9999', '212-555-0000']
print(phoneNumRegex.findall("Cell: 415-555-9999 Work: 212-555-0000"))

phoneNumRegex = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)")
print(phoneNumRegex.findall("Cell: 415-555-9999 Work: 212-555-0000"))


# CHARATER CLASSES
xmasRegex = re.compile(r"\d+\s\w+")
print(xmasRegex.findall(
    "12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge"))

# Making Your Own Character Classes
# [a-zA-Z0-9] will match all lowercase letters, uppercase letters, and numbers.
vowelRegex = re.compile(r"[aeiouAEIOU]")
print(vowelRegex.findall("RoboCop eats baby food. BABY FOOD."))


# By placing a caret character (^) just after the character class’s opening bracket, you can make a negative character class. A negative character class will match all the characters that are not in the character class.
consonantRegex = re.compile(r"[^aeiouAEIOU]")
print(consonantRegex.findall("RoboCop eats baby food. BABY FOOD."))

# The Caret and Dollar Sign Characters
# the caret symbol (^) at the start of a regex to indicate that a match must occur at the beginning of the searched text
beginsWithHello = re.compile(r"^Hello")
print(beginsWithHello.search("Hello, world!"))


# The r'\d$' regular expression string matches strings that end with a numeric character from 0 to 9.
endsWithNumber = re.compile(r"\d$")
print(endsWithNumber.search("Your number is 42"))
print(endsWithNumber.search("Your number is forty two.") == None)


# The Wildcard Character
atRegex = re.compile(r".at")
print(atRegex.findall("The cat in the hat sat on the flat mat"))

# Matching everything with DOT-STAR
# By default its greedy
nameRegex = re.compile(r"First Name: (.*)Last Name: (.*)")
mo = nameRegex.search("First Name: Al Last Name: Sweigart")
print(mo.group(1))
print(mo.group(2))

# Non-greedy
nongreedyHaRegex = re.compile(r"<.*?>")
mo = nongreedyHaRegex.search("<To serve man>for dinner.>")
print(mo.group())  # Output: <To serve man>

# Greedy
greedyHaRegex = re.compile(r"<.*>")
mo = greedyHaRegex.search("<To serve man>for dinner.>")
print(mo.group())


# Matching Newlins with the DOT character
noNewlineRegex = re.compile(".*")
print(noNewlineRegex.search(
    "Serve the public trust.\nProtect the innocent.\nUphold the law.").group())

newlineRegex = re.compile(".*", re.DOTALL)
print(newlineRegex.search(
    "Serve the public trust.\nProtect the innocent.\nUphold the law.").group())


# Case Insensitive Matching
robocop = re.compile(r"robocop", re.I)
print(robocop.search("RoboCop is part man, part machine, all cop.").group())


# SUBSTITUTING STRING WITH SUB() METHOD
namesRegex = re.compile(r"Agent \w+")
print(namesRegex.sub("CENSORED", "Agent Alice gave the secret documents to Agent Bob."))

agentNamesRegex = re.compile(r"Agent (\w)\w*")
print(agentNamesRegex.sub(r"\1****",
                          "Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent."))


# Managing Complex Regex
phoneNumRegex = re.compile(
    r"((\d{3}|\(d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)")

# COMBINING RE.IGNORECASE, RE.DOTALL, AND RE.VERBOSE
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
