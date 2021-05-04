import os
from os import system 
import array as arr 
import math 

system('cls')
# index = length (size) - 1, first element is 0

# to create an array in Python, use (...[..])

#                              0  1  2  3  4  5  6
integerArray = arr.array('i', [1, 3, 7, 6, 8, 2, 5])
floatArray = arr.array('f', [2.6, 3.5, 8.9])

# length of the array
integerArrayLength = len(integerArray)

for index in range(integerArrayLength):
    print(integerArray[index])


print('-----------------------------')
print('------- Integer Array -------')
# Print the first element of the array
print(f'Element 1 = {integerArray[0]}')
# Print the second element of the array
print(f'Element 2 = {integerArray[1]}')
# Print the third element of the array
print(f'Element 3 = {integerArray[2]}')
print('-----------------------------')
print()
print('-----------------------------')
print('-------- Float Array --------')
# Print the first element of the array
print(f'Element 1 = {round(floatArray[0], 2)}')
# Print the second element of the array
print(f'Element 2 = {floatArray[1]}')
# Print the third element of the array
print(f'Element 3 = {round(floatArray[2], 2)}')
print('-----------------------------')

# Print the last element of the integerArray
print(f'Last Element = {integerArray[-1]}')
# Print from the 4th element to the end
print(f'Element from 4th to the end = {integerArray[3:]}')
# Print elements from 1 to 3
print(f'Elements from 1 to 3 = {integerArray[:-4]}') # 4 is not included
# Print elements from 2 to 4
print(f'Elements from 2 to 4 = {integerArray[1:4]}') # 1 is not included
# Print the last 4 elements
print(f'Last 4 Elements= {integerArray[-4:]}')

# Print the second element and third to last [3, 8]
print(integerArray[1::3])