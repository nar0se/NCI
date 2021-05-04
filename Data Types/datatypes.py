import os
from os import system
from colorama import Fore, Back, Style

system('cls')

integerNumber = 4 # => integer type with 32 bits => 4 bytes
longNumber = 12344543534534534545345435345345 # => long type with 64 bits => 8 bytes
floatNumber = 2.54 # => float type with 32 bits => 4 bytes
string1 = "My dog is beautiful" # => string type, string is a class
string2 = "56" # "" makes 56 a string
isTrue = True # => boolean type
isStudent = False
isConnected = False
isInClass = True
a = 'A'

print(Fore.CYAN, f'''
        Integer => {integerNumber} 
        Long => {longNumber}
        Float => {floatNumber}
        String 1 => {string1}
        String 2 => {string2}
        Boolean 1 => {isTrue}
        Boolean 2 => {isStudent}
        Boolean 3 => {isConnected}
        Boolean 4 => {isInClass}
        String => {a}
''')

print(Style.RESET_ALL) # resets colors back to normal
print(Fore.RED) # set the font to RED
print(type(integerNumber)) # prints the type of integerNumber => returns <class 'int'>
print(type(longNumber)) # prints the type of longNumber => returns <class 'int'>
print(type(isTrue)) # prints the type of isTrue => returns <class 'bool'>
print(type(string1)) # prints the type of string1 => returns <class 'str'>
print(type(a))

print(Style.RESET_ALL)
print(Fore.YELLOW)
print(f'The type of string2 is {type(string2)}')
print(f'The type of string2 is NOW {type(int(string2))}') # casting, to change a type to another

#(Back.) => lists what colors you can choose in Fore

print(Style.RESET_ALL)
print(Fore.GREEN)
tuples = (1, 2, 3 , 4 , 5, 1 , 2, 8 , 9) # => size of this tuple is 8, index size -1
print(type(tuples))

for number in tuples:
    print(type(number))

print (f'First element of the tuples tuple is {tuples[0]}')
print (f'Seventh element of the tuples tuple is {tuples[6]}')

# Assignment
counter = 1

print('--------------------------------------------------------')
number_of_iterations = int(input('Please enter the # of iterations >> '))

for i in range (number_of_iterations):
    print('Value of count is {}'.format(counter))
    #counter += 1 # counter = counter + 1
    #counter *= 2 # counter = counter * 2
    #counter -= 10 # counter = counter - 10
    counter /= 5 # counter - counter / 5