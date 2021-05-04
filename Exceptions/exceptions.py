import os
from os import system
from colorama import Fore, Style

system('clear')

num1 = int(input('Enter a number >> '))
num2 = int(input('Enter another number >> '))

# handle exceptions using try/except

try:
   division = round(num1 / num2, 2)
   print('Division = {}'.format(division))
except ZeroDivisionError as err:
    print(err)
# this executes regarless of whether an exception ocurrs or not
finally: print(Fore.RED, 'I am in the finally block', Style.RESET_ALL)
#except ZeroDivisionError: print(f'Division {num2} is not allowed')

print('I am here now after exception is caught')


try:
    num = int(input('Enter a number >> '))
    print(f'You entered {num}')
except ValueError as err:
    print(err)
#except ValueError: int(input('Invalid type. Try again >> '))

# Check this page out for more on exception handling
# https://docs.python.org/3.9/tutorial/errors.html#exceptions