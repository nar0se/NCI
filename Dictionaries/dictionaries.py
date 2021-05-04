import os 
from os import system
system('cls')


myNewDictionary = {
    'Integer': 4,
    'Float': 3.6,
    'String': 'This is a dictionary in Python',
    'Boolean': True,
    'FirstName': 'Antonio',
    'LastName': 'Banderas',
    'Age': 58    
}

# Print every element of the dictionary myNewDictionary
print(myNewDictionary)

# print first element of the dictionary myNewDictionary
print(f"First Element -> {myNewDictionary['Integer']}")
print(f"First Element -> {myNewDictionary.get('Integer')}")

keys = myNewDictionary.keys()
print('---- Keys ----')
print(keys)
print()
values = myNewDictionary.values()
print('---- Values ----')
print(values)
print()
print('---- Keys and Values ----')
print(f'{keys} - {values}')

# print every value given the key
print()
for key in myNewDictionary:
    print(myNewDictionary[key])

print()
for key in myNewDictionary:
    print(f'{key}: {myNewDictionary[key]}')

# prints every element given key and value
print()
for key, value in myNewDictionary.items():
    print(f'{key}: {value}')


# Add another key to the dictionary
myNewDictionary['Phone'] = '1234567890'

print()
print('-------- New Key Added -----------')
for key, value in myNewDictionary.items():
    print(f'{key}: {value}')


dictionaryList = []
print()
print()
number_of_people = int(input('Enter how many people >> '))
counter = 1
for i in range(number_of_people):
    myEmptyDictionary = {}
    print()
    print(f'Person # {counter}: ')
    fname = input('Enter your first name >> ')
    myEmptyDictionary['FirstName'] = fname
    lname = input('Enter your last name >> ')
    myEmptyDictionary['LastName'] = lname
    age = int(input('Enter your age >> '))
    myEmptyDictionary['Age'] = age
    phone = input('Enter your phone >> ')
    myEmptyDictionary['Phone'] = phone
    gpa = float(input('Enter your gpa >> '))
    myEmptyDictionary['GPA'] = gpa
    subject = input('Enter your subject >> ')
    myEmptyDictionary['Subject'] = subject
    major = input('Enter your major >> ')
    myEmptyDictionary['Major'] = major
    dictionaryList.append(myEmptyDictionary)
    counter += 1


dictCounter = 1
for dictionary in dictionaryList:
    print()
    print(f'---- Dictionary # {dictCounter} ----')
    for key, value in dictionary.items():        
        print(f'{key}: {value}')
    dictCounter += 1