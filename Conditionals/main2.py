import os 
from os import system
import functions as f 

system('cls')

# variable declaration
maxGallonQt = 15
lowGallonQt = 2
isARental = False # flag


currentStatus = float(input('Please take a look at your gas gauge and tell us how many gallons you think you have left >> '))
response = int(input('Is this a rental? [1 for Yes or 2 for No] >> '))

if response == 1:
    isARental = True 
else:
    isARental


if not isARental:
    if (currentStatus < 0 or currentStatus > maxGallonQt):
        print(f'Invalid entry. Are you blind or do you just not know your car? Your car does not take {currentStatus} gallons')
    else:
        f.conditional_decided(currentStatus, lowGallonQt)
else:
    if (currentStatus < 0 or currentStatus > maxGallonQt):
        print('Invalid entry. You have been automatically forgiven bc this is not your car. Please check again')
    else:
        f.conditional_decided(currentStatus, lowGallonQt)


f.printHello('Hello, hello, hello')
addition = f.printAddition(8, 10)
print(f'Addition: {addition}')

f.printTest()