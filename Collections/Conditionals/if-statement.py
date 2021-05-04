import os
from os import system 

system('cls')

num = int(input('Enter a number >> '))

if (num > 10):
    print('{} is greater than 10'.format(num))

print('----------------------------')
num2 = int(input('Enter another number >> '))

# calculate modulus to find remainder
if (num2 % 2 == 0):
    print('{} is an even number'.format(num2))

if (num2 % 2 == 1):
    print('{} is an odd number'.format(num2))