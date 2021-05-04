import os
from os import system
import math
from math import pow

system('cls')

# a CUSTOM function can take as many arguments as you want
def calculate(n1, n2):
    print('''
    THESE ARE THE OPERATIONS
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Modulus
    6. Exponentiation''')
    choice = int(input('Select one above [1 - 6] >> '))
    if(choice == 1):
        addition = n1 + n2
        return addition, 'addition'
    elif (choice == 2):
        subtraction = n1 - n2
        return subtraction, 'subtraction'
    elif (choice == 3):
        multiplication = n1 * n2
        return multiplication, 'multiplication'
    elif (choice == 4):
        division = n1/n2
        return division, 'division'
    elif (choice == 5):
        modulus = n1 % n2
        return modulus, 'modulus'
    elif (choice == 6):
        exponentiation = pow(n1, n2)
        return exponentiation, 'exponentiation'
    else:
        return 0, 'Invalid Entry'
        


while True:
    system('clear')
    num1 = int(input('Enter a number >> '))
    num2 = int(input('Enter another number >> '))
    returnedValue, operation= calculate(num1, num2)
    if(operation == 'Invalid Entry'):
        print(f'Returned Value is {returnedValue}. We cannot show any result of this operation. Try again later')
        break
    print(f'The {operation} of {num1} and {num2} is {returnedValue}')
    print(' ')
    response = input('Do you want to enter other numbers? [Y/N] >> ')
    while True:
        if(response.upper() == 'Y' or response.upper() == 'N'):
            break
        else:
            print('Invalid response. Try again')
            response = input('Do you want to enter other numbers? [Y/N] >> ')
    if (response.upper() == 'N'):
        print('Thank you for using our humble calculator. Have a great day!!!')
        break

# def returnWhatEverIWant():
#     return 'Pushpa', 'Omer', 'Rachid', 'Mtagui'

# p, o, r, m = returnWhatEverIWant()

# print(f'The names you returned are: {p}, {o}, {r}, and {m}')