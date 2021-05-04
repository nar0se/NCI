import os 
from os import system
from colorama import Fore, Style
system('clear')

# print a string with single quotes
print('This is single quotes -> ', Fore.RED, '\'Really?\'', Style.RESET_ALL)
# print a string with double quotes inside
print("This is double quotes inside -> ", Fore.RED, "\"Double Quotes Inside\"",  Style.RESET_ALL)
# print a string with double quotes
print("It's just -> ", Fore.RED, "\"Double Quotes\"", Style.RESET_ALL)
# print a string with triple quotes
print(Fore.BLUE, '''
    \'''Triple Quotes\'''
''', Style.RESET_ALL)

fname = 'Carlos'
lname = 'Garcia'

print(fname + ' ' + lname) # concatenation => Carlos Garcia

length = 4
print(f'hi{length}') # => another way to concatenate

# **** ASSIGNMENT ****
name1 = 'Carlos' # => name1 = Carlos
name2 = name1 # name2 = Carlos
name3 = name2 # name3 = Carlos
print(name3)

# **** RE-ASSIGNMENT ****
name3 = 'Benito' # name3 = Benito
name1 = name3 # name1 = Benito
name2 = name1 # name 2 = Benito

print(name2) # this returns Benito 
print(name1) # this returns Benito 
print(name3) # this returns Benito 

name1 = 'Pedro'
name4 = 'Antonio'
name3 = 'Carlos'
name2 = name3
name4 = name2
name1 = name4

print("What is value of name4?") 
print(f'name4 is {name4}') # returns name4 is Carlos
print("What is value of name1?")
print(f'name1 is {name1}') # returns name1 is Carlos

apple = '4'
orange = '6'
print(apple + orange) # returns 46

text = 'I am'
text1 = 'happy'
print(text + text1) # this returns I amhappy

apple = int('4') # apple is of type int
orange = int('6') # orange is of type int
print(apple + orange) # this returns 10

num1 = '100'
num2 = '50'
print(num1 + num2) # returns '100' + '50' = '10050'

print(type('100')) # returns <class 'str'>
print(type('50')) # returns <class 'str'>
print(type(100)) # returns <class 'int'>
print(type(True)) # returns <class 'bool'>
print(type(10.0)) # returns <class 'float'>
print(type(int(float('5.6')))) # returns <class 'int'>
print(type(str(float(int(float('6.5')))))) # returns <class 'str'>
print(float(int(float(int(float(int(float('18.2'))))))))
#      18.0  18  18.0  18  18.0  18  18.2
#     <----------------------------------  '18.2'