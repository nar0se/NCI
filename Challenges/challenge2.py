import os
from os import system 

system('cls')


# 1. Create an empty list

integerList = []
    
# 2. Add 10 strings to it


breakoutList = ['Priya0', 'Priya1', 'Nathan2', 'Nathan3', 'Yordi4', 'Yordi5', 'Namratha6', 'Namratha7', 'Priyanka8', 'Priyanka9'] 

# 3. Remove string # 7

breakoutList.remove(breakoutList[6])

# 4. Print strings 3 - 6

print(breakoutList[2:7])
print('-----------------------------------')

# 5. Print the last 5 strings

length=len(breakoutList)
for index in range(4,length):   
    print(f'{breakoutList[index]}')
print('-----------------------------------')

# 6. Print the last string

print(breakoutList[-1])
print('-----------------------------------')

# 7. Replace string 5 with 'I am here'

somename = breakoutList[4] = 'I am here!'
print(somename)
print('-----------------------------------')

# 8. Insert 'I am being inserted' at position 4
breakoutList.insert(3,'I am being inserted')
print(breakoutList)
print('-----------------------------------')

# 9. Delete strings 2 and 7

breakoutList.remove(breakoutList[1])
breakoutList.remove(breakoutList[6])
print(breakoutList)


# 10. Create a set and print it

PythonSet = {'Arrays', 'Dictionaries', 'Lists', 'Sets'}
for items in PythonSet:
    print(items)
print('-----------------------------------')


# 11. Create three tuples and print the elements in them

boolTuple = (False, False, False, True)
stringTuple = ('string', 'thing', 'yarn', 'darn')
numberTuple = (3, 2, 1, 0.0)
print(boolTuple)
print(stringTuple)
print(numberTuple)
print('-----------------------------------')


# 12. Create three dictionaries and print the elements in them

myDictionary = {
    # key      value
    'Column1': 'Column2',
    'English': 'Hello',
    'Spanish': 'Hola',
    'Hindi': 'Namaste'
}
print('')
print('---Dictionary 1---')
for key in myDictionary:
    print(f'{key}: {myDictionary[key]}')
print('                        ***** ')

print('')
print('---Dictionary 2---')
myDictionary2 = {
    'City': 'Manaynay',
    'State': 'VA',
    'Zip': '20109'
}
print('   Horizontal (um, no.):')
print(myDictionary2)

print('')
print('   Vertical (much better [for dictionaries]!):')
for key in myDictionary2:
    print(f'{key}: {myDictionary2[key]}')
print('                        ***** ')

print('')
myDictionary3 = {
    'Line 1': 'Testing - 1, 2, 3!',
    'Line 2 (spaces)': '   Blahhhhhhhhhhhh.   ',
    'Line 3 (First Name Last Name)': 'Blah Blah',
    'Line 4 (Last Name, First Name)': 'Blah, Blah',
    'Line 5 (Full Name with "Nickname")': 'Blah "BLAH" Blah'
}
print('---Dictionary 3---')
for key in myDictionary3:
    print(f'{key}: {myDictionary3.get(key)}')
print('-----------------------------------')

# 13. Have the user enter a name and a grade. Print 'F' if the grade is less than 60, 'D' between 61-70, 'C' between 71-80, 'B' between 81-90, and
# 'A' between 91-100. A grade entered in any range not included above, the program should print invalid option. 
    # If grade is 70 and name is 'Carlos', take the student to detention; Carlos has misbehaved recently. 

print('')
name = input('Enter your name (LETTERS ONLY): ')
print('')
grade = float(input('Your [numerical] grade, please: '))
print('')

if grade < 60:
    print('')
    print('"F" for FAILURE. {}, you are a FAIL. Fail, fail, faiL.'.format(name))
elif grade >=61 and grade <=70:
    print('')
    print('Your grade of {} is a "D" for "Do better."'.format(grade))
elif (grade >=71 and grade<=80):
    print('')
    print('Your grade of {} is a C, which falls in the AVERAGE range. {}, you are just average.'.format(grade, name))
elif grade>=81 and grade<=90:
    print('')
    print('B... "B" for "Better than a C."')
elif grade >=91 and grade<=100:
    print('')
    print('YAYYYYY. {} You have an A!!!'.format(name))
else:
    print('{} is an invalid option'.format(grade))
if name == 'Carlos' and grade==70:
    print('')
    print('Because your name is {} \nAND you have a {}, \nyou must report to detention... AHORA MISMO. \n\nYou have misbehaved recently.'.format(name, grade))
    print('-----------------------------------')


# 13. BONUS: Create two lists with size 10, one list of names, 
    #and the other list with ages. Declare an empty dictionary and populate it with the two lists. Hint: The list of names is the key and the list of ages is the value [e.g. 'Carlos': 45]


names = ['Thing1', 'Thing2', 'Thing3', 'Thing4', 'Thing5', 'Thing6', 'Thing7', 'Thing8', 'Thing9', 'Thing10']
ages = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print('Names List:')
for keys in names:
    print(keys)
print('')

print('Ages List:')
for values in ages:
    print(values)
print('')

EmptyDictionary = {}
print('My Empty Dictionary:')
print('')
print(EmptyDictionary)
print('')

for items in names and ages:
        #res = dict(zip(test_keys, test_values))
    EmptyDictionary = dict(zip(names, ages))
print ("Filled Dictionary (raw): " +  str(EmptyDictionary))
        # FYI: "dict" before (res) won't work; has to be "str" >> e.g., print ("Resultant dictionary is : " +  dict(res))
print('')

print('Filled Dictionary (final - vertical!):')
for key in EmptyDictionary:
    print(f'{key}: {EmptyDictionary[key]}')
print('-----------------------------------')

# Professor's Solution

myNewDictionary = {}
numberOfPeople = int(input('How many people do you want to add to my list? >> '))
counter = 1

for index in range(numberOfPeople):
    print(f'Person # {counter}: ')
    name = input('Enter the name >> ')
    age = int(input('Enter age >> '))
    myNewDictionary[name] = age
    counter+=1

for key, value in myNewDictionary.items():
    print(f"'{key}': {value}")