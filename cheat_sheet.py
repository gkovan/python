print("This is a cheat sheet to learn python data structures.")

#### Python Map using dictionary

map_of_romans: dict[str, int]  = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

sum_of_romans = map_of_romans['X'] + map_of_romans['V']
assert sum_of_romans == 15

print(map_of_romans)

# Method 1: Direct assignment using square brackets
map_of_romans['A'] = 1000

# Method 2: Using update() method with a single key-value pair
map_of_romans.update({'B': 2000})

# Method 3: Using update() method with multiple key-value pairs
map_of_romans.update({'E': 3000, 'F': 4000})

# Method 4: Using setdefault() - sets value only if key doesn't exist
map_of_romans.setdefault('G', 5000)

print(map_of_romans)

# 7. Iterating
for key in map_of_romans:  # Keys
    print(key)

for value in map_of_romans.values():  # Values
    print(value)

for key, value in map_of_romans.items():  # Both
    print(f"{key}: {value}")

###### SETS

# Create a new set
my_set: set[int] = set()

# Add element to set (returns None in Python)
my_set_add_result = my_set.add(1)  # Note: Python's add() doesn't return boolean
assert 1 in my_set  # Verify element was added

print(my_set)

# Check if element exists in set
my_set_contains_result = 1 in my_set  # Python uses 'in' operator instead of contains()
assert my_set_contains_result == True

# Alternative ways to create a set:
# From a list
my_set = set([1, 2, 3])
print(f"set using a list:  {my_set}")

# Using set literal
my_set = {1, 2, 3}
print(f"set using a literal {my_set}")

########### QUEUE
from collections import deque

# Create a new queue
my_queue = deque()

# Add elements to queue
my_queue.append(1)  # enqueue
my_queue.append(2)  # enqueue

print(my_queue)

# Remove element from front of queue
my_queue.popleft()  # dequeue (removes and returns 1)

print(my_queue)

########### Arrays

# Create an array (list in Python)
my_array: list[int] = [1, 2, 3, 50, 8, 15, 6]

# Sort the array
my_array.sort()  # sorts in-place
# OR
sorted_array: list[int] = sorted(my_array)  # creates a new sorted list

# Resize array (extend with None values)
original_size: int  = len(my_array)
my_array.extend([None] * (100 - original_size))
assert len(my_array) == 100

# Convert array to list (in Python, arrays are already lists)
my_list: list[int]  = my_array  # direct assignment as they're the same type
# OR for a new copy:
my_list = my_array.copy()
assert len(my_list) == 100

# Initialize a list with values
initialized_list = [1, 2, 3, 4]
assert len(initialized_list) == 4

# If you need a more array-like structure (with fixed type), you can use numpy:
import numpy as np

# Create and sort numpy array
np_array = np.array([1, 2, 3, 50, 8, 15, 6])
print(np_array)
np_array.sort()
print(np_array)

# Resize numpy array
np_array = np.resize(np_array, 100)
assert len(np_array) == 100

# Convert numpy array to list
list_from_np = np_array.tolist()


######### Kwargs (key word arguments)

# Basic kwargs example
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Call with any number of keyword arguments
print_kwargs(name="John", age=30, city="New York")
# Output:
# name: John
# age: 30
# city: New York

# Combining regular parameters with kwargs
def mixed_function(required_param, *args, **kwargs):
    print(f"Required: {required_param}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

mixed_function("Hello", 1, 2, 3, name="John", age=30)
# Output:
# Required: Hello
# Args: (1, 2, 3)
# Kwargs: {'name': 'John', 'age': 30}

# Using kwargs to pass arguments to another function
def wrapper_function(**kwargs):
    return another_function(**kwargs)  # Unpacks kwargs

def another_function(x, y, z):
    return x + y + z

result = wrapper_function(x=1, y=2, z=3)
print(result)  # Output: 6

# Real-world example: configurable function
def create_user(**user_data):
    defaults = {
        'active': True,
        'role': 'user'
    }
    # Update defaults with provided values
    defaults.update(user_data)
    return defaults

# Different ways to call the function
user1 = create_user(name="John", email="john@example.com")
user2 = create_user(name="Jane", email="jane@example.com", role="admin")

print(user1)  # {'active': True, 'role': 'user', 'name': 'John', 'email': 'john@example.com'}
print(user2)  # {'active': True, 'role': 'admin', 'name': 'Jane', 'email': 'jane@example.com'}

# Class example with kwargs
class User:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', 'Anonymous')
        self.age = kwargs.get('age', 0)
        self.city = kwargs.get('city', 'Unknown')

# Create instances with different parameters
user1 = User(name="John", age=30)
print(f"{user1.name} {user1.age} {user1.city}")
user2 = User(name="Jane", age=25, city="London")
print(f"{user2.name} {user2.age} {user2.city}")

# Dictionary unpacking with kwargs
def process_data(**kwargs):
    print(kwargs)

data_dict = {'name': 'John', 'age': 30}
process_data(**data_dict)  # Unpacks dictionary to kwargs

############## Positional arguments

# As a parameter (packing)
def sum_numbers(*args):
    print("GK")
    print(args)
    return sum(args)

print(sum_numbers(1, 2, 3))  # Output: 6
print(sum_numbers(1, 2, 3, 4, 5))  # Output: 15

# As an argument (unpacking)
numbers = [1, 2, 3]
print(sum_numbers(*numbers))  # Output: 6

# Function that can take any number of arguments
def create_user(*fields, **properties):
    required_fields = fields
    user_properties = properties
    # Process the user creation
    return {"fields": required_fields, "properties": user_properties}

# Different ways to call
user_abc = create_user("name", "email", age=25, active=True)
print(user_abc)
user_def = create_user(*["name", "email"], **{"age": 25, "active": True})
print(user_def)

# Java Collections and Python

# Key differences from Java:

# Python uses lists instead of ArrayList
# No explicit Collections utility class needed
# Many operations are methods of list object
# Python uses list comprehensions instead of streams
# Swapping is done with tuple unpacking
# Binary search requires bisect module
# No type declarations needed

# Creating and adding elements to list
my_kids = []
my_kids.extend(["Daniel", "Eliana", "Michaela", "David"])

# Print each kid (equivalent to forEach)
for kid in my_kids:
    print(kid)

# Using list comprehension or map for uppercase (equivalent to stream.map)
my_kids_upper = [kid.upper() for kid in my_kids]
print(my_kids_upper)
# OR using map
for kid in map(str.upper, my_kids):
    print(kid)

# Sort in ascending order
ages = [15, 8, 47, 11, 13, 37]
ages.sort()  # sorts in place
print(ages)
# OR
sorted_ages = sorted(ages, reverse=True)  # creates new sorted list
print(sorted_ages)

# Binary search
from bisect import bisect_left

# Note: list must be sorted for binary search
def binary_search(lst, target):
    idx = bisect_left(lst, target)
    if idx < len(lst) and lst[idx] == target:
        return idx
    return -1

# Find element
found = binary_search(ages, 15)
print(f"Found returns the index of the element in list: {found}")

not_found = binary_search(ages, 7)
print(f"Not found returns -1: {not_found}")

################ Conversions

# Key differences from Java:
# Python uses built-in functions (int(), str(), etc.) instead of class methods
# No explicit type declarations needed
# Python strings are immutable like Java Strings
# Python doesn't have a separate character type (single characters are strings of length 1)
# Python's type conversion is generally more straightforward
# Some additional useful Python conversions:

# Convert string to integer
my_int = int("85")
assert my_int == 85

# Convert integer to string
assert str(my_int) == "85"

# Convert character to its numeric value
c1 = '9'
i1 = int(c1)  # direct conversion
# OR
i1 = ord(c1) - ord('0')  # using ASCII values
assert i1 == 9

# Additional Python conversion examples:
# String to float
float_num = float("85.5")
assert float_num == 85.5

# String to boolean
bool_val = bool("True")
assert bool_val is True

# Integer to binary string
binary = bin(85)  # returns '0b1010101'
binary_without_prefix = bin(85)[2:]  # returns '1010101'

# Integer to hex string
hex_string = hex(85)  # returns '0x55'
hex_without_prefix = hex(85)[2:]  # returns '55'

# Character to ASCII value
ascii_val = ord('A')  # returns 65

# ASCII value to character
char_val = chr(65)  # returns 'A'

# List of strings to list of integers
str_list = ["1", "2", "3"]
int_list = [int(x) for x in str_list]
assert int_list == [1, 2, 3]

# Join list of integers into string
numbers = [1, 2, 3]
string_numbers = "".join(map(str, numbers))
assert string_numbers == "123"

# Some additional useful Python conversions:

# Round float to integer
rounded = round(85.6)  # returns 86

# Convert to absolute value
abs_val = abs(-85)  # returns 85

# Convert string to list of characters
char_list = list("Hello")  # returns ['H', 'e', 'l', 'l', 'o']

# Convert multiple strings to integers
x, y, z = map(int, ["1", "2", "3"])
assert x == 1 and y == 2 and z == 3

# Format number as string with specific width
formatted = f"{85:03d}"  # returns "085"

# Format float with specific precision
formatted_float = f"{3.14159:.2f}"  # returns "3.14"

# Convert string to title case
title = "hello world".title()  # returns "Hello World"

# Convert string to uppercase/lowercase
upper = "hello".upper()  # returns "HELLO"
lower = "HELLO".lower()  # returns "hello"

########### Map Reduce in Python

from functools import reduce

# Basic map with built-in function
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Map with multiple iterables
list1 = [1, 2, 3]
list2 = [10, 20, 30]
sums = list(map(lambda x, y: x + y, list1, list2))
print(sums)  # [11, 22, 33]

# Map with regular function
def multiply_by_two(x):
    return x * 2

doubled = list(map(multiply_by_two, numbers))
print(doubled)  # [2, 4, 6, 8, 10]
