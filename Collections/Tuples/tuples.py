import os
from os import system

system('cls')

# To create a tuple, use (...)

integerTuple = (3, 5, 7, 2, 4)  # tuple of integers
floatTuple = (2.5, 4.6, 7.5, 1.8) # tuple of floats
boolTuple = (True, False, False, True) # tuple of booleans
stringTuple = ('word', 'sentence', 'syllable', 'letter') # tuple of strings
isTrue = False

# print the integerTuple
for i in integerTuple:
    print(f'Integer value is {i}')

print(integerTuple)
print(type(integerTuple))

if (type(isTrue) == bool):
    print('The value is a boolean')
else:
    print('The value is NOT a boolean')