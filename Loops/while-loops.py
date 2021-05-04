import os 
from os import system
system('cls')

counter = 0
hiCounter = 0

while counter < 10: 
    print(f'{hiCounter + 1}. Hi')
    hiCounter += 1
    counter += 1
    

attemptsCounter = 3

 # do while => at 1 time it executed
while True:
    input(' Login >> ')
    if (attemptsCounter == 1):
        break 
    print(f'You have {attemptsCounter - 1} attempts left')
    attemptsCounter -= 1

system('clear')

while True:
    num = int(input('Enter a number between 1 and 3 >> '))
    if (num >= 1 and num <= 3):
        print('valid entry')
        break


system('clear')

people = []
namesCounter = 0
listCounter = 1
names = int(input('How many names do you want to add to the roster? >> ')) # 5

while namesCounter < names:
    print('*******************************')
    print(f'Enter full name # {listCounter}')
    fname = input('Enter your first name >> ')
    lname = input('Enter your last name >> ')
    price = float(input('Enter a price >> '))
    fullName = fname + ' ' + lname + '      - $' + str(price)
    people.append(fullName)
    namesCounter += 1
    listCounter += 1


namesListCounter = 1

print()
print('Full Name ..........Salary')
for person in people:
    print(f'{namesListCounter}. {person}')
    namesListCounter += 1