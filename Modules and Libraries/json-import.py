import json, os
from json import dumps, loads
from os import system

system('cls')

# this will change a number to string
num = 15
print(f'type of {num} is {type(num)}')
result = dumps(num)
print(f'type of {result} is NOW {type(result)}')

# this will change a string to a number
result2 = loads(result)
print(f'type of {result2} is NOW {type(result2)}')

# turns a list into a string
lists = [2, 4, 5, 6]
listToString = dumps(lists)
print(f'type of {lists} is NOW {type(listToString)}')

# turns the string back to a list
stringToList = loads(listToString)
print(f'type of {lists} is NOW {type(stringToList)}')