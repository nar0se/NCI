import os
from os import system 

system('cls')

# To create a dictionary, use {} but it's a key-value pair
# dictionaries allow duplicates
# they are ordered, in other words, order is guaranteed

myDictionary = {
    # key      value
    'fruit1': 'apple',
    'fruit2': 'mango',
    'fruit3': 'kiwi1',
    'fruit4': 'kiwi2',
}

# --- Two different ways to print a dictionary
# 1. name_of_dictionary[key_name] => prints value

for key in myDictionary:
    print(f'{key}: {myDictionary[key]}')

#print(myDictionary['fruit1'])

print ('--------------------------------')
# name_of_dictionary.get(key) => print the value
for key in myDictionary:
    print(f'{key}: {myDictionary.get(key)}')

print(myDictionary.get('fruit2'))