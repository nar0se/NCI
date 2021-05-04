import os
from os import system
from colorama import Fore, Style
system('clear')

# 1. Bryan -> Give a demo of nested loops (please make it different from the one
# in class)

for i in range(10):
    print(Fore.RED, f'i...... {i}')
    for j in range(5):
        print(Fore.CYAN, f'j.... {j}')

print(Style.RESET_ALL)
# 2. Shweta -> Give a demo of nested if statements

x = 10
if (x > 8):
    if( x == 10):
        print(f'x == {x}')


# 3. Yukta -> Create a function that accepts different types and print the values

def printDifferentTypes(*args):
    for type in args:
        print(type)

printDifferentTypes(
    'Carlos', 
    34, 
    5.6, 
    [2, 3, 5, 6, 7], 
    (4, 5, 8, 1, 9),
    {
        'name': 'Benito',
        'age': 45,
        'phone': '1234567890'
    },
    {
        4, 6, 7, 8, 9
    }, 
    True)


# 4. Donovan -> List of dictionaries (3) [manually]
[
    {
        'name': 'Carlos',
        'age':67
    },
    {
        'phone': '1234567890',
        'address': '123 Main St Miami, FL 33173'
    },
    {
        'subject': 'Math',
        'grade': 98.5
    }
]

# 5. Fatine -> give a demo of nested while loops (3)

outerCounter = 0
innerCounter = 0
while outerCounter < 10:
    print(f'Outer Counter ..... {outerCounter}')
    while innerCounter < 5:
        print(f'Inner ...... {innerCounter}')
        innerCounter += 1
    outerCounter += 1
    


# 6. Namratha -> Give a demo of exceptions
x = 1
y = 0
result = 0
try:
    result = x / 0
except ZeroDivisionError as err: print('Error Message:', err)


# 7. Rafil -> in a list from 1 to 20, print all numbers except 9, 13
for i in range(1, 21):
    if (i == 9 or i == 13):
       continue
    print(i)