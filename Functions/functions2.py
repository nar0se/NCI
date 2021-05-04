import os
from os import system

# function that return something are called fruitful
# function that do not return anything are called non fruitful
system('clear')

# this is a very simple function, no arguments
def printName():
    return 'Your name is Richard'


printName()
name = input('What is your name? >> ')
if(name == 'Richard'):
    print(printName())
    # print('Your name is Richard')
    returnString = printName()
    print(returnString)
else:
    print('sorry, I do not recognize this name')

# -- Demo 
a = 3
b = 2
c = 1

def demo():
    y = (a + b + c)
    return y # makes this function fruitful (return statement)
print(demo())
returnInt = demo()
print(returnInt)

print(returnInt + 4)
print(demo() + 4)
# -- End of Demo


# return more than 1 value
def returnSeveralValuesPrint():
    num1 = 5
    num2 = 2
    subtraction = num1 - num2
    return num1, num2, subtraction, 'Omer'
    
n1, n2, add, name = returnSeveralValuesPrint()

print('n1 = > ', n1)
print('n2 = > ', n2)
print('add = > ', add)
print(f'Your name is {name}')
# ----------------------------

# optional arguments, != not equal operator
def optionArgumentPrint(args = None):
    if (args != None): 
        print(f"Argument has been passed and is '{args}'")
    else:
        print('No argument has been passed')
optionArgumentPrint() # passing no value
optionArgumentPrint('I am passed') # passing a value


# call the function as many times as you want
def add(n1, n2):
    addition = n1 + n2
    return addition

print(add(4, 6))
print(add(8, 2))
print(add(9, 5))
print(add(10, 11))

# example of built-in functions in python
# open()
# round()
# ceil()
# floor()
# system()
# format()
# print()
# type()
# fabs()
# sum()
# dict()

myString = 'Hello how are you?'
newString = myString.split(" ")
print(newString)
for word in newString:
    print(word)
print(type(newString))
#() => tuples
# {} => dictionaries and sets, 
# [] => lists
# (...[]) => arrays