# Write an application for Cody's Car Care Shop that shows a user a list of available services:
# - Oil Change
# - Tire Rotation
# - Battery Check
# - Brake Inspection
# ​
# Allow the user to enter a string that corresponds to one of the options and display the option
# and its price as $25, $22, $15, or $5, accordingly. Display an error message if the user enters
# an invalid item. 
# ​
# It might not be reasonable to expect users to type long entries such as 'Oil Change' accurately. 
#  as long as the user enters the first three characters of service, the choice is considered valid. 
# ​
# Create a list with all the available services and another with the list of prices in another
#  file and import them to the main file. 
# ​
# Create a list of lists and print all elements of every list
# ​
# Create a list containing lists of tuple, an array, two dictionaries, a set, two strings, two floats, two integers, two 
#  booleans. Print each element of the list

import json, os
from json import dumps, loads 
from os import system
# from prices import *
# from services import *

system('cls')

counter = 0

path = './Challenges/services.txt'

services = ['Oil Change', 'Tire Rotation', 'Battery Check', 'Brake Inspection']
with open (path, 'w') as file:
    file.write('This is the list of services we provide')
    file.close()
with open(path, 'a') as file:
        file.write(f'\n{services}')
        file.close()

path = './Challenges/prices.txt'

prices = ['25', '22', '15', '5']
with open(path, 'w') as file:
    file.write('This is the list of prices for our services')
    file.close()
with open(path, 'a') as file:
        file.write(f'\n{prices}')
        file.close()

cselect = str(input('Please select one of our services >> '))
dselect = cselect.lower()
string = dselect[0:3]


if (string) == 'oil':
    string = services[0]
print(string)
elif (string) == 'tir':
    string = services[1]
elif (string) == 'bat':
    string = services[2]
elif (string) == 'bra':
    string = services[3]

listofservices = dumps(services)
print(listofservices)
listofprices = dumps(prices)
print(listofprices)

listoflists = [
    ['Oil Change', 'Tire Rotation', 'Battery Check', 'Brake Inspection']
    ['25', '22', '15', '5']
]


# while True:
#     content = input('What content do you want to add to the file? >> ')
#     with open(path, 'a') as file:
#         file.write(f'\n{content}')
#         file.close()
#     response = input('Do you want to add more content [Y/N]? >> ')
#     if(str.upper(response) == 'N'):
#         break







