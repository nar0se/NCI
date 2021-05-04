import os
from os import system
import array as arr

system('cls')

name = 'benito'
print('---- Original Name ----')
print(name)

print('---- Capitalized Name ----')
newName = name.capitalize()
print(newName)

print()
print('-------- List --------')
addressList = []
addressList.append('Carlos')
addressList.append('Miami')
addressList.append('33183')
addressList.append(True)

print(addressList)
for adrs in addressList:
    print(adrs)
print()

# Fatine -> Set and print it

print('-------- Set --------')
months = {'January', 'February', 'March', 'April'}
for month in months:
    print(month)

print()
# Nathan -> Tuple and print
print('-------- Tuple --------')
monthsTuple = ('January', 'February', 'March', 'April')
print('Months:')
for m in monthsTuple:
    print(f'''
           {m}''')

# Donovan -> Dictionary and print it
print()
print('-------- Dictionary --------')
myNewDictionary = {
    "month1": "January",
    "month2": "February",
    "month3": "March",
    "month4": "April"
}
print('---- One Way ----')
for month in myNewDictionary:
    print(f'{month}: {myNewDictionary[month]}')
print('--- Another way ----')
for month in myNewDictionary:
    print(f'{month}: {myNewDictionary.get(month)}')
print('--- Even another way ----')
for key, value in myNewDictionary.items():
    print(f'{key}: {value}')

# Bryan -> Array and print it
print()
print('-------- Array --------')
integer_array = arr.array('i', [1, -2, 3, 8, 9, 5, 7, 6])
print('---- One Way ----')
for index in range(len(integer_array)):
    print(integer_array[index])
print('--- Another way ----')
integer_array = arr.array('i', [1, -2, 3, 8, 9, 5, 7, 6])
for e in integer_array:
    print(e)

# Bonus -> Create a tuple of integers and print
# the sum of all the integers in the tuple

print()
print('-------- Sum of Integers in Tuple --------')
numTuple = (12, 20, 1, 4, 6, 7, 8)
addition = 0
print('---- One Way ----')
for num in numTuple:
    addition += num
print(addition)
print('--- Another way ----')
print(sum(numTuple))
print('--- Even another way ----')
print(sum(list(numTuple)))

addition1 = 0
print('--- Even Even another way ----')
for num in numTuple: addition1 += num
print(addition1)

# 0 = 0 + 12   -> 12
# 12 = 12 + 20 -> 32
# 32 = 32 + 1 -> 33
# 33 = 33 + 4 -> 37
# 37 = 37 + 6 -> 43
# 43 = 43 + 7 -> 50
# 50 = 50 + 8 -> 58
# = 58