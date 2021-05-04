import os
from os import system


system('cls')
print()
print()

def calculate(a1):
    print(a1)

def calculate(*args):
    print(a1, a2)

def calculate(a1, a2 = None, a3 = None):
    print(a1, a2, a3)

def calculate(a1, a2 = None, a3 = None, a4 = None):
    print(a1, a2, a3, a4)

# calculate(1)
# calculate(1, 2)
# calculate(1, 2, 3)
# calculate(1, 2, 3, 4)






# This will accept any number and types of values you send
def printArgs(*args):
    for a in args:
        print(a)
 
printArgs('Dunieski', 'Wendy', 'Priya')
printArgs(25, 2)
printArgs(3.6, 2.8)
printArgs(True, False)
printArgs('Dunieski', 3.7, 45, [4, 5, 6, 7], (3, 4, 5, 6), ('i', [3, 4, 5, 6, 6]), 
{
    'name': 'Carlos',
    'age': 34
}, {2, 3, 4, 5} )

printArgs([2, 3, 4, 5, 6], [4, 6, 8,])