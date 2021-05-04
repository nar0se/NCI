import os, math
from os import system 
from colorama import Fore, Back, Style 
from math import pow 

system('cls')

isNotZero = False 

# --- Functions ----
#        2     3
def add(num1, num2):
    addCalculate = num1 + num2 
 #  addCalculate = 2    +   3 
    return addCalculate
#   return 5

def subtract(num1, num2):
    subtractCalculate = num1 - num2
    return subtractCalculate

def multiply(num1, num2):
    multiplyCalculate = num1 * num2 
    return multiplyCalculate

def divide(num1, num2):
    if (num2 == 0):
        try:
           divideCalculate = num1 / num2
        except ZeroDivisionError: print(f'Not possible division by {n2}')
    else:
        divideCalculate = num1 / num2
        return divideCalculate

def printModulus(num1, num2):
    modulusCalculate = num1 % num2
    return modulusCalculate

def powerOf1(num1, num2):
    exponent = num1 ** num2
    return exponent

def powerOf2(num1, num2):
    exponent = pow(n1, n2)
    return exponent

def printName(fname, lname, age):
    print(f'{fname} {lname}!! Cool name! I like it!!! and you are {age} years old')
# -------------------

# ----------- User input -----
n1 = int(input('Enter first number >> '))
n2 = int(input('Enter second number >> '))
fname = input("What is your first name? >> ")
lname = input("What is your last name? >> ")
age = int(input("What is your age? >> "))
# -------- end of User input ----

# ---- Calling functions -----
#          add(2, 3)
addition = add(n1, n2) # n1 and n2 are arguments
#          --  5  ---
subtraction = subtract(n1, n2)
multiplication = multiply(n1, n2)
division = divide(n1, n2)
modulus = printModulus(n1, n2)
exponent1 = powerOf1(n1, n2)
exponent2 = powerOf2(n1, n2)




# ---- end of calling functions -----

print(f'The sum of {n1} and {n2} is {addition}')
print(f'The subtraction of {n1} and {n2} is {subtraction}')
print(f'The multiplication of {n1} and {n2} is {multiplication}')
print(f'The division of {n1} and {n2} is {division}')
print(f'The modulus from division of {n1} and {n2} is {modulus}')
print(f'{n1} elevated to the power of {n2} is {exponent1} from function powerOf1')
print(f'{n1} elevated to the power of {n2} is {exponent2} from function powerOf2')

print()
print("---------------------------------")
printName(fname, lname, age)
print("---------------------------------")