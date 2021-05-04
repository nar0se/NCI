import os
from os import system

system('cls')

# sort() => it sorts the list
# count() => it counts every element in the list, it takes one argument => count('element')
# copy() => it copies the list to another list
# insert() => it inserts elements to a list at a specific index ('index', 'element') => it takes two arguments
# reverse() => it reverses the list
# append() => it appends info/elements to the list
# remove() => it removes a specific element from the list => it takes one argument => remove('element')
# pop() => it deletes the last element of the list
# clear => it clears the list (it empties it out)
# del => deletes specific elements in a list by index => del list['index']

numbers = [12, 4, 5, 6, 2, 1, 9, 2, 0, 22, 26]

print('--------- USING THE sort() FUNCTION ----------')
print('List without yet invoking the sort() function: \n{}'.format(numbers))
numbers.sort()
print('List after invoking the sort() function: \n{}'.format(numbers))
print('--------------------------------------------')

print()
print('--------- USING THE count() FUNCTION ----------')
print(numbers)
for number in numbers:
    print('{} is counted {} times'.format(number, numbers.count(number)))

print()
print('--------- USING THE copy() FUNCTION ----------')
print('Original list: \n{}'.format(numbers))
numbers1 = numbers.copy()
print('Copied list: \n{}'.format(numbers1))

print()
print('--------- USING THE insert() FUNCTION ----------')
print('List without yet invoking the insert() function: \n{}'.format(numbers))
# numbers.insert(index, value)
numbers.insert(2, 20)
print('List after invoking the insert() function: \n{}'.format(numbers))
print('-------------------------------------------------')

print()
print('--------- USING THE reverse() FUNCTION ----------')
print('List without yet invoking the reverse() function: \n{}'.format(numbers))
numbers.reverse()
print('List after invoking the reverse() function: \n{}'.format(numbers))
print('-------------------------------------------------')
print()
print('--------- USING THE append() FUNCTION ----------')
print('List without yet invoking the append() function: \n{}'.format(numbers))
numbers.append(15)
numbers.append(22)
print('List after using the append() function and adding 15 and 22: \n{}'.format(numbers))
print('-------------------------------------------------')
print()
print('--------- USING THE remove() FUNCTION ----------')
print('List without yet invoking the remove() function: \n{}'.format(numbers))
numbers.remove(20)
print('List after using the remove() function and removing 20: \n{}'.format(numbers))
print('-------------------------------------------------')
print()
print('--------- USING THE pop() FUNCTION ----------')
print('List without yet invoking the pop() function: \n{}'.format(numbers))
numbers.pop()
print('List after using the pop() function: \n{}'.format(numbers))
print('-------------------------------------------------')
print()
print('------------------- USING del ------------------')
print('List without yet invoking the del() function: \n{}'.format(numbers))
del numbers[2:5]
print('List after using del and deleting elements from 2 to 4: \n{}'.format(numbers))
del numbers[:2]
print('List after using del and deleting all elements before index 2 \n{}'.format(numbers))
del numbers[4:]
print('List after using del and deleting all elements after index 3 (excluding 3) \n{}'.format(numbers))
del numbers[-2]
print('List after using del and deleting the element taking 2 place from the last element \n{}'.format(numbers))
del numbers[-2:]
print('List after using del and deleting the last 2 elements of the list \n{}'.format(numbers))
print('-------------------------------------------------')

print()
print('--------- USING THE clear() FUNCTION ----------') 
print('List without yet invoking the clear() function: \n{}'.format(numbers))
numbers.clear()
print('List after using the clear() function: \n{}'.format(numbers))
print('-------------------------------------------------')

# print('THIS IS A FLOAT THAT WE WANT')
# listOfFloats = [3.2, 4.4, 5.7, 5.7, 7.4, 8.2, 9.0]
# for fl in listOfFloats:
#  print(listOfFloats.count(fl))
# print('RIGHT HERE^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

print()
print()
numbers3= [3, 5, 6, 7, 3, 2, 3, 5, 6, 7, 8, 9, 0, 4]
print(numbers3)
del numbers3[-2]
print(numbers3)

listOfNames = ['Williams', 'Dunieski', 'Moron']
print(listOfNames)
listOfNames.sort()
print(listOfNames)