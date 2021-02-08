##### Variables #####

# Python naming convention uses
# lowercase letter and underscores
from timeit import timeit
from pprint import pprint
from sys import getsizeof
from array import array
from collections import deque
import math
students_count = 1000  # Integer
rating = 3.99  # Floating point number
is_published = False  # Boolean
course_name = "Python Crash Course"  # String

# Multiple lines
x, y = 1, 2

# Multiple variable with same value
x = y = 1

##### Dynamic Typing #####
print(type(students_count))  # Know the type of a variable

##### Type Annotation ######
age: int = 20
# age = "Python"  # MyPy linter is giving an error because of typing annotation

##### Mutable and Immutable #####
x = 1
print(id(x))
x = x + 1
print(id(x))
# Primitive Type are immutable (value cannot change), which mean
# python will allocate a new memory slot for the value.
# Hence why the id change.

# List are mutable type (the memory address doesn't change )
z = [1, 2, 3]
print(id(z))
z.append(4)
print(id(z))

##### Strings #####
course = "Python Programming"

# Length of a string
len(course)

# Access char with []
print(course[0])

# end of string with -1
print(course[-1])

# Slicing
print(course[0:3])  # 3 not included

# Espaces sequences
# \" "
# \' '
# \\ '
# \n line break
message = "     Python \" Programming   "

message = """      Using
Line break      """

print(message)

firstName = "Will"
lastName = "Pepino"

# Formatted strings
fullName = f"{firstName} {lastName}"

# Can be used with any function
nameLength = f"{len(firstName)} + {len(lastName)}"
print(fullName)
print(nameLength)

# Useful String Methods
print(course.upper())
print(course.lower())
print(course.title())

# Remove whitespace in front of string
print(message.strip())

# find pro in programming
print(course.find("Pro"))

# Replace in a string
print(course.replace("P", "-"))

# is there programming in course ?
print("Programming" in course)

# is there not programming in course ?
print("Programming" not in course)


##### numbers #####
x = 10  # decimal
y = 0b10  # binary
zz = 0x12c  # hex

print(zz)  # print decimal
print(bin(x))  # print binary

print(hex(x))  # print hex

# Complex numbers
X = 1 + 2j  # use j as a imaginary number

print(X)

# add
x = 10 + 3
# sub
x = 10 - 3
# multi
x = 10 * 3
# div
x = 10 / 3
# div integer
x = 10 // 3
# modulus
x = 10 % 3
# power
x = 10 ** 3

# augmented assignement operator
x -= 1
x += 1
x *= 1
x /= 3
x //= 3
x %= 3
x **= 3

# constant by convention (uppercase letter)
PI = 3.14

# round a number
round(PI)

# absolute
abs(PI)


math.floor(PI)

# all math function https://docs.python.org/3/library/math.html

# Type conversion
# x = input("x: ")

int(x)
float(x)

bool(x)
# Falsy value
# ""
# 0
# []
# None (null)

str(x)

# Conditional #

age = 22
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")

print("All done")

# inline if
message = "Eligible" if age >= 18 else "Not eligible"


##### Loop #####
# for loop
for letter in "Python":
    print(letter)

# while loop
for letter in ['a', 'b', 'b']:
    print(letter)

for x in range(5):
    print(x)

print("---------------")
# from 2 to 9
for x in range(2, 10):
    print(x)

print("---------------")
# even numbers using (step)
for x in range(0, 10, 2):
    print(x)

# range does not return a list
print(range(5))
print(type(range(5)))  # class range

# this is a list
print([1, 2, 3, 4, 5])

names = ["John", "Mary"]

# Loop
## For ##
for name in names:
    if name.startswith("J"):
        print("found")
        break
else:
    print("Not found")

## While ##
# guess = 0
# answer = 5
# while answer != guess:
#     guess = int(input("Guess :"))

# function

# define variable


def increment(number: int, by: int = 1) -> tuple:
    return (number, number + by)


# keyword argument (make code readable)
increment(2, by=3)

# add args

# use endless args

# args as tuple (xargs)


# object as user (dictionnary) (xxargs)


def save_user(**user):
    print(user)
    print(user['id'])


save_user(id=1, name='admin')


# Scope
message = "a"


def greet():
    if True:
        global message  # modify global variable (do not use)
        message = "b"  # else it creates a local variable
    print(message)


greet()
print(message)


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("start")

print("finish")
print(multiply(1, 2, 3))


def fizz_buzz(input):

    if input % 3 == 0 and input % 5 == 0:
        return 'fizzbuzz'
    if input % 3 == 0:
        return 'fizz'
    if input % 5 == 0:
        return 'buzz'
    return input

    # if / 3 return fizz
    # if / 5 return buzz
    # if both return fizz buzz
    # else return 7
print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(30))
print(fizz_buzz(7))


##### Data structure #####

### lists ###

letters = ['a', 'b', 'c']

matrix = [[0, 1], [2, 3]]

zeros = [0] * 5  # 5 zeros in a list

combined = zeros + letters  # combination of 2 lists

print(combined)

numbers = list(range(20))  # create a list made out of an iterable

print(numbers)

chars = list("Hello World")  # list creates a list from any iterable

print(chars)

print(letters[0])

print(letters[-1])

firstLetters = letters[0:3]

print(firstLetters)


print(numbers[::2])  # skip interval

print(numbers[::-1])  # all the items in reverse

# unpacking a list
# prefix variable with * means all other (xargs)
first, second, third, *other = numbers

print(other)

first, *other, last = numbers  # getting the last item

print(first)
print(second)
print(third)
print(last)
print(other)

# is equal to
first = numbers[0]
second = numbers[1]
third = numbers[2]

# When you enumerate a list, Python gives a Tuple with the index and the value
for letter in enumerate(letters):
    print(letter)

# you can unpack directly in for statement
for index, letter in enumerate(letters):
    print(index, letter)

# if you don't need the index
for letter in letters:
    print(letter)


# Add
letters.append("d")
print(letters)

# add at index
letters.insert(0, "-")

# Remove
letters.pop()

# Remove at index
letters.pop(0)

# Remove first occurence of letter
letters.remove("b")

# remove a range of item
del letters[0:3]

# clear
letters.clear()

# find the index
letters = ['a', 'b', 'c']
print(letters.index('c'))  # error if not in letters

print(letters.count('d'))  # count the occurence


numbers = [3, 51, 2, 8, 6]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

print(sorted(numbers))

items = [
    ("Product1", 10),
    ("product2", 9),
    ("Product3", 12),
]

# cant sort with traditional sort function

# Sort function

# do not do, use lambda


def sort_item(item):
    return item[1]


# sort using a function
items.sort(key=sort_item)

print(items)


# Lambda function (improving sort) # does the same thing as line 421 to 428
items.sort(key=lambda item: item[1])

# Do not do, use map
# prices = []
# for items in items:
#     prices.append(item[1])

# Map function using lambda
prices = list(map(lambda item: item[1], items))
print(prices)

# Filter function using lambda
filtered = list(filter(lambda item: item[1] >= 10, items))

print(filtered)

### Comprehension ###
# Example of map using comprehension
prices = [item[1] for item in items]  # BEST PRACTICE
# [expression for item in items] # apply an expression for each item in the list
print(prices)

# Example of filter using comprehension
filtered = [item for item in items if item[1] >= 10]  # BEST PRACTICE

### Zip function ###
list1 = [1, 2, 3]
list2 = [10, 20, 30]

# turn into tuple
print(list(zip('abc', list1, list2)))


### Stack ###
browsing_session = []
browsing_session.append(1)  # Add Item to stack
browsing_session.append(2)  # Add Item to stack
last = browsing_session.pop()  # Remove last item
print(last)
print(browsing_session)
first = browsing_session[-1]  # peek last item
if not browsing_session:  # if is empty
    pass

### Queue ###
que = deque([])  # using import deque

que.append(1)
que.append(2)
que.append(3)
que.popleft()
print(que)
if not que:
    print("empty")

### Tuple ###
point = (1, 2) * 3 + (3, 4)
print(point)

# works the same as a list but readonly

x, y, z, *other = point

# Swapping variable
x = 10
y = 11
# old way of swapping variable
z = x
x = y
y = z

x, y = y, x  # SWAPPING VARIABLE LIKE A BOSS

##### ARRAYS #####
# DIFFERENCE WITH LIST IS THAT EVERY VARIABLE IS TYPED
intArray = array('i', [1, 2, 3])  # i is type

intArray.append(1)
intArray.insert(1, 1)  # index
intArray.pop()  # Remove
print(intArray[2])


##### Sets #####
# only unique item
numbers = [1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 3, 4, 5, 5, 6, 7]
first = set(numbers)

second = {1, 4, 8}

# Union of 2 sets (or)
print(first | second)

# Union of 2 sets (and)
print(first & second)

# difference of 2 sets
print(first - second)

# in first or second but not both
print(first ^ second)

# Set does not support indexing

# print(first[0]) impossible

# Check if item in list
if 1 in first:
    print('yes')

### Dictionaries ###
# Key value pair
point = {"x": 1, "y": 2}

point = dict(x=1, y=2)

print(point["x"])
point["z"] = 30

if "a" in point:
    print(point["a"])

print(point.get("a"))  # return none if doesnt exist
print(point.get("a", 0))  # return 0 if doesnt exist

del point['x']  # del a key
print(point)

for key in point:
    print(key, point[key])

for x in point.items():
    print(x)

for key, value in point.items():
    print(key, value)

### Dictionary Comprehensions ###
# for a list
values = [x * 2 for x in range(5)]
print(values)

# for a dictionary \ no key for value
values = {x * 2 for x in range(5)}
print(values)

# with key as x
values = {x: x * 2 for x in range(5)}
print(values)

##### Generator Expression #####
# generator object

values = (x * 2 for x in range(10000000))
print(values)  # generator object iterable
# what is interesting is the size is very small because they are computed values
print('gen:', getsizeof(values))
values = [x * 2 for x in range(10000000)]
print("list:", getsizeof(values))


### Unpacking operator ###
numbers = [1, 2, 3]


values = list(range(5))  # Same as
values = [*range(5)]

# same with strings
values = [*"This is a string transformed into a list"]

print(*numbers)  # same as ... in javascript (spread operator)

first = {'x': 1}
second = {'x': 10, 'y': 2}
combined = {**first, **second, 'z': 1}
print(combined)


# FIND THE MOST REPEATED CHAR
sentence = "This is a common interview question"

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

print(char_frequency)

pprint(char_frequency, width=1)

char_frequency_sorted = (
    sorted(char_frequency.items(), key=lambda kv: kv[1], reverse=True))
print(char_frequency_sorted[0])


### Exceptions ###
## and with statement #
try:
    # with syntax automatically closes the file
    with open("app.py") as file:
        print("File opened")  # with statement
        file.__enter__  # Context management protocol (can use with)
        file.__exit__  # Context management protocol (can use with)
        # If the object has __enter__ and __exit__ it means we can use "with ... as file:"
    # age = int(input("Age: "))
    # xfactor = 10 / age
except (ValueError, ZeroDivisionError) as e:
    print("You didn't enter a valid age")
    print(e)
    print(type(e))
except ZeroDivisionError:
    print("age cannot be 0")
else:
    print("No exceptions were thrown.")
finally:
    print("Always executed")
    # file.close() no need for this line of code using with syntax

print("Execution continues.")

# raise exception
code1 = """
def calc_xfactor(age):
    if age <= 0:
        raise ValueError('Age cannot be lesser or equal to 0.')  # costly
    return 10/age


try:
    calc_xfactor(-1)
except ValueError as e:
    pass
"""
code2 = """
def calc_xfactor(age):
    if age <= 0:
        return None
    return 10/age

xfactor = calc_xfactor(-1)
if xfactor == None:
    pass
"""
# calculate method time
print(timeit(code1, number=100000000))  # only works using python3 in terminal
print(timeit(code2, number=100000000))  # only works using python3 in terminal
