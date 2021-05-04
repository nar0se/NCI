import os
from os import system 

system('cls')

# To create a list, use [...]

# list of strings

fruitList = ['apple', 'banana', 'cherry']
fruitListLength = len(fruitList)
 # list of integers
integerList = [3, 5, 2, 7]
integerListLength = len(integerList)
#list of floats
floatList = [2.5, 3.1, 4.8]
floatListLength = len(floatList)

# Print the lists
for fruit in fruitList:
    print(fruit)

for integer in integerList:
    print(integer)

for f in floatList:
    print(f)

print(f'First element of the fruit list is {fruitList[0]}')
print(f'The size of fruitList is {fruitListLength}')
print(f'The size of integerList is {integerListLength}')
print(f'The size of floatList is {floatListLength}')

# index              0          1      2    3           4        5     6
personInfoList = ['Carlos', 'Garcia', 25, '1329', '1234567890', 3.8, True]
personInfoListLength = len(personInfoList)

print('------ Person Info List ------')
for index in range(personInfoListLength):
    print(personInfoList[index])
#                         index = 0 -> personInfoList[0] =      Carlos
#   index + 1 -> 0 + 1 -> index = 1 -> personInfoList[1] =      Garcia
#   index + 1 -> 1 + 1 -> index = 2 -> personInfoList[2] =      25
#   index + 1 -> 2 + 1 -> index = 3 -> personInfoList[3] =      1329
#   index + 1 -> 3 + 1 -> index = 4 -> personInfoList[4] =      1234567890
#   index + 1 -> 4 + 1 -> index = 5 -> personInfoList[5] =      3.8
#   index + 1 -> 5 + 1 -> index = 6 -> personInfoList[6] =      True
    print(personInfoList[index])

# print the second element of the personInfoList
print(f'Second element of the personInfoList => {personInfoList[1]}')

for index in range(fruitListLength):
    if (index == 0):
        print(f'First element of fruitList => {fruitList[index]}')
    if (index == 1):
        print(f'Second element of integerList => {integerList[index]}')
    if (index == 2 ):
        print(f'Third element of floatList => {floatList[index]}')

print()
# Add a fruit to the fruitList
# using the append() function
# anatomy of the append() -> list_name.append(element)

def printList(l):
    for element in l:
        print(element)

print('---- Fruit List before Appending ----')
printList(fruitList)
print('---- Fruit List After Appending ----')
fruitList.append('orange')
printList(fruitList)
print()
print('---- Integer List before Appending ----')
printList(integerList)
print('---- Integer List After Appending ----')
integerList.append(14)
printList(integerList)
print('---- Float List before Appending ----')
printList(floatList)
print('---- Float List After Appending ----')
floatList.append(89.7)
printList(floatList)
print()

gradesList = []
tuples = (89.5, 78.6, 91.5, 78.9, 80.3)
print('---- Grade List ----')
printList(gradesList)
print('---- Grade List Populated ----')
# for every element (e) of the tuple tuples, append it to the gradeList
for e in tuples:
    gradesList.append(e)
printList(gradesList)

# Delete a specific element in the Fruit List
print()
print('---- Fruit List before deleting the second element -> banana ----')
printList(fruitList)
print('---- Fruit List after deleting the second element -> banana ----')
fruitList.remove(fruitList[1])
printList(fruitList)

# Insert an element using insert(position, element)
print()
print('---- Fruit List before inserting element at position 2 -> kiwi ----')
printList(fruitList)
print('---- Fruit List after inserting element at position 2 -> kiwi ----')
fruitList.insert(2, 'kiwi')
printList(fruitList)

# Replace element -> reassigning a value
print()
print('---- Fruit List before replacing element at position 0 -> apple ----')
printList(fruitList)
print('---- Fruit List before replacing element at position 0 -> apple ----')
fruitList[0] = 'pineapple'
printList(fruitList)

# replace every element in the list
print()
print('---- Fruit List before replacing every single element ----')
printList(fruitList)
fruitTuple = ('grapes', 'grapefuit', 'tangerine', 'guava')
for index in range(len(fruitList)):
    fruitList[index] = fruitTuple[index]
    # pineapple <- grapes
    # pineapple gets replaced for grapes
    # cherry gets replaced for grapefruit
    # kiwi gets replaced for tangerine
    # orange gets replaced for guava

print('---- Fruit List after replacing every single element ----')
printList(fruitList)