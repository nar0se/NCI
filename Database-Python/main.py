import os  
from os import system 
import operations as ops


system('cls')

operationsList = ['Read', 'Insert', 'Update', 'Delete']

counter = 1
print('These are the operations that you can perform in our database: ')
for operation in operationsList:
    print(f'{counter}. {operation}')
    counter += 1
choice = int(input('Select one above >> '))

if (choice == 1):
    ops.readUserOperation()
elif (choice == 2):
    ops.insertOperation()
elif (choice == 3):
    ops.updateOperation()
elif (choice == 4):
    ops.deleteOperation()
else:
    print('invalid selection')