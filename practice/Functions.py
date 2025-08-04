def greet():
    print("Hello, Ritvik!")

greet()  # Calling the function

#Function with Parameters
def greet_user(name):
    print("Hello,", name)

greet_user("Ritvik")

#Function with Return
def add(x, y):
    return x + y

result = add(5, 3)
print(result)  # Output: 8


#Default Parameter Values
def welcome(name="User"):
    print("Welcome", name)

welcome()        # Output: Welcome User
welcome("Ritvik")  # Output: Welcome Ritvik



#Keyword Arguments
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=21, name="Ritvik")


#Variable Number of Arguments
# *args → multiple positional arguments

def total(*nums):
    print(sum(nums))

total(10, 20, 30)  # Output: 60


#**kwargs → multiple keyword arguments

def show_details(**data):
    for key, value in data.items():
        print(key, ":", value)

show_details(name="Ritvik", age=22)


'''
Anonymous Functions – lambda
A lambda function is a one-line anonymous function,
used for simple operations where using def might feel too heavy.
'''

#lambda arguments : expression -- syntax

square = lambda x: x * x
print(square(5))  # Output: 25


#map() Function
#Applies a function to each item in a sequence.
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, nums))
print(squares)  # [1, 4, 9, 16]

'''
 filter() Function
Filters elements of an iterable based on a condition (boolean function).
'''
nums = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)  # [2, 4, 6]


'''
reduce() Function (from functools module)
Performs a cumulative operation on the items in a list.
'''
from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)  # Output: 24


'''
Recursion
A function calling itself. Used for problems that can be broken into smaller sub-problems 
(like factorial, Fibonacci, etc.)
'''

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120


'''
Scope of Variables
Type	Scope
Local	Inside the function only
Global	Declared outside, accessible everywhere
global	Used inside a function to modify global variables
'''

x = 10

def change():
    global x
    x = 20

change()
print(x)  # Output: 20


