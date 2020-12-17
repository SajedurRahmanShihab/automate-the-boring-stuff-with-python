# Getting Individual Values in a List with Indexes
import copy
import random
spam = ["cat", "bat", "rat", "elephant"]
print(spam[0])

# Negative Indexes
print(spam[-1])

# Getting a List from Another List with Slices
print(spam[0:4])
print(spam[1:3])
print(len(spam))

# List Concatenation and List Replication
print([1, 2, 3] + ["A", "B", "C"])
print(["X", "Y", "Z"] * 3)


# Working with LISTS
personNames = []
while True:
    print("Enter the name of cat" + str(len(personNames)+1) +
          "(Or enter nothing to stop.):")
    name = input()
    if name == "":
        break
    personNames = personNames + [name]

print("The person names are: ")
for name in personNames:
    print(" " + name)


# Using for loops with lists
supplies = ["pens", "staplers", "flmethrowers", "binders"]
for i in range(len(supplies)):
    print("Index " + str(i) + " in supplies is: " + supplies[i])

# The in and not in Operators
print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])


# The Multiple Assignment Trick
cat = ['fat', 'gray', 'loud']
size, color, disposition = cat

# Using the enumerate() Function with Lists
supplies = ["pens", "staplers", "flamethrowers", "binders"]
for index, items in enumerate(supplies):
    print("Index " + str(index) + " in supplies is: " + items)


# Using the random.choice() and random.shuffle() Functions with Lists
pets = ["Dog", "Cat", "Mouse"]
print(random.choice(pets))

people = ['Alice', 'Bob', 'Carol', 'David']
random.shuffle(people)
print(people)

# Augmented Assignment Operators
spam = 42
spam += 1
print(spam)


# Finding a Value in a List with the index() Method
spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hello'))


# Adding Values to Lists with the append() and insert() Methods
spam = ["cat", "dog", "bat"]
spam.append("moose")
print(spam)
spam.insert(1, "chicken")
print(spam)


# Removing Values from Lists with the remove() Method
spam.remove("bat")
print(spam)

# Sorting the Values in a List with the sort() Method
spam = [2, 5, 3, 14, 1, -7]
spam.sort()
print(spam)


# Reversing the Values in a List with the reverse() Method
spam = ["cat", "dog", "moose"]
spam.reverse()
print(spam)

# EXAMPLE PROGRAM: MAGIC 8 BALL WITH A LIST
messages = [
    "It is certain",
    "Yes definitely",
    "Reply hazy try again",
    "Ask again later",
    "Concentrate and ask again",
    "My reply is no",
    "Outlook not so good",
    "Very doubtful"
]

print(messages[random.randint(0, len(messages) - 1)])

# Sequence Data Types
name = "Zophie"
print(name[0])


# Mutable and Immutable Data Types
name = "Zophie a cat"
# name[7] = "the" cause an error


# The proper way to “mutate” a string is to use slicing and concatenation to build a new string by copying from parts of the old string
name = "Zophie a cat"
newName = name[0:7] + "the" + name[8:12]
print(name)
print(newName)


# The Tuple Data Types
eggs = ("hello", 42, 0.5)
print(eggs[0])

# Converting Types with the list() and tuple() Functions
print(tuple(["cat", "dog", 5]))
print(list(("cat", "dog", 5)))


# REFERENCES
spam = 42
cheese = spam
spam = 100
print(spam)
print(cheese)


spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = "Hello!"
print(spam)
print(cheese)


# Identity and the id() Function
print(id("Howdy"))
bacon = "Hello"
print(id(bacon))
bacon += "world!"
print(id(bacon))

# Passing References


def eggs1(someParameter):
    someParameter.append("Hello")


spam = [1, 2, 3]
eggs1(spam)
print(spam)


# The copy Module's copy() and deepcopy() Function
spam = ["A", "B", "C", "D"]
print(id(spam))
cheese = copy.copy(spam)
print(id(cheese))  # cheese is different list with different identiy.
cheese[1] = 42
print(spam)
print(cheese)


# A SHORT PROGRAM: CONWAYS GAME OF LIFE
# Have to complete it

# Practice Question
"""
1. What is []?
Ans:
It's a list

2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
Ans:
spam = [2, 4, 6, 8, 10]
spam.insert(2, "hello")

3. What does spam[int(int('3' * 2) // 11)] evaluate to?
Ans:
ERROR

4. What does spam[-1] evaluate to?
Ans:
Return last value of list

5. What does spam[:2] evaluate to?
Ans:
Return value of index 0, 1 of list

For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].

6. What does bacon.index('cat') evaluate to?
Answer: 1

7. What does bacon.append(99) make the list value in bacon look like?
Answer: [3.14, 'cat', 11, 'cat', True, 99]

8.  What does bacon.remove('cat') make the list value in bacon look like?
Answer: [3.14, 11, 'cat', True, 99]

9. What are the operators for list concatenation and list replication?
Answer:
concatenation +
replication copy

10. What is the difference between the append() and insert() list methods?
Answer:
append() add item at the end of the list
insert() add item at specific index in list

11. What are two ways to remove values from a list?
Ans:
pop()
remove()

12.  Name a few ways that list values are similar to string values.
Didn't understand the question

13. What is the difference between lists and tuples?
Answer:
list mutable, allow duplicate values
tuple immutable

14. How do you type the tuple value that has just the integer value 42 in it?
Answer:
tuple(42)

15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?
Answer:
aTuple = (123, 'xyz', 'zara', 'abc');
listTotuple = list(aTuple)
myTuple = tuple(listToTuple)

16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
Answer:
Reference

17. What is the difference between copy.copy() and copy.deepcopy()?
Answer:
copy() allows to duplicate a list not just its reference
deepcopy() suitable when list contains list, deepcopy() copy inner list




"""
