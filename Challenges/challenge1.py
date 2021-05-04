import os, statistics
from os import system
from statistics import mean 

system('clear')

# 1. Create 4 variables of a different type each and assign values to them
print('------------------------------------------------------------------------')
print('1. Create 4 variables of a different type each and assign values to them')
print('------------------------------------------------------------------------')
print('Variables are created in the program')
name = 'Carlos' # string
num1 = 12345677842234566786543 # long
isHere = False # boolean
num2 = 4 # integer
print()
# 2. Print the type of each variable
print('------------------------------------------------------------------------')
print('2. Print the type of each variable')
print('------------------------------------------------------------------------')
print(f'''
    name: {name} 
    type: {type(name)}
    num1: {num1}
    type: {type(num1)}
    num2: {num2} 
    type: {type(num2)}
    isHere: {isHere} 
    type: {type(isHere)}
''')

print()
# 3. Ask a user to enter new values and reassign those values to the variables created above
print('------------------------------------------------------------------------')
print('3. Ask a user to enter new values and reassign those values to the variables created above')
print('------------------------------------------------------------------------')
name = input('Enter a different name >> ')
num1 = int(input('Enter a number >> '))
num2 = int(input('Enter another number >> '))
isHere = bool(input('Enter True >> '))

print(f'''
    name: {name} 
    type: {type(name)}
    num1: {num1}
    type: {type(num1)}
    num2: {num2} 
    type: {type(num2)}
    isHere: {isHere} 
    type: {type(isHere)}
''')
print()
# 4. Ask the user to input first name, last name, school name, the grades of three different subjects
print('------------------------------------------------------------------------')
print('4, 5. Ask the user to input first name, last name, school name, the grades of three different subjects')
print('------------------------------------------------------------------------')
def printStudentInfo(fn, ln, sn):
    print(f'''
        Student's Info:
        ---------------
        First Name: {fn}
        Last Name: {ln}
        School Name: {sn}
        ----------------
    ''')

fname = input('Enter your first name >> ')
lname = input('Enter your last name >> ')
schoolName = input('Enter your school name >> ')
subject1 = float(input('Enter subject 1 grade >> '))
subject2 = float(input('Enter subject 2 grade >> '))
subject3 = float(input('Enter subject 3 grade >> '))

printStudentInfo(fname, lname, schoolName)

print()

# 6. Create another function that calculates and returns the average grade of the student
print('------------------------------------------------------------------------')
print('6. Create another function that calculates and returns the average grade of the student')
print('------------------------------------------------------------------------')

# user-defined function
def calculateAverage(s1, s2, s3):
    avg = (s1 + s2 + s3) / 3
    return round(avg, 2) 

average= calculateAverage(subject1, subject2, subject3)
print(f'The grade average for {fname} {lname} is {average}')
print()

tup = (subject1, subject2, subject3)
# mean(tup)
print(f'The average of tup is {round(mean(tup), 2)}')

print('------------------------------------------------------------------------')
print(''''
  7. With your prior knowledge of Linux for loops, do some research and do the following:
        a) Print all even numbers from 1 to 30
        b) Print all odd number from 1 to 50
  ''')
print('------------------------------------------------------------------------')

# even numbers
print('EVEN NUMBERS')
for i in range(31):
    if (i % 2 == 0):
        print(i)

print('ODD NUMBERS')
# odd numbers
for i in range(50):
    if(i % 2 == 1):
        print(i)


print('------------------------------------------------------------------------')
print('8. Using the knowledge of casting acquired today in class, convert a String to an Integer and print the type to confirm')
print('------------------------------------------------------------------------')
string1 = '78'
print(f'The type of string1 before conversion is {type(string1)}')
convertedString = int(string1) # casting
print(f'The type of string1 is NOW {type(convertedString)}') 
print()


print('------------------------------------------------------------------------')
print("9, 10. Call a function and pass the following values ('I', 'love', 'Programming', 'because', 'it's', 'cool')")
def concatenate(s1, s2, s3, s4, s5, s6):
    return f'{s1} {s2} {s3} {s4} {s5} {s6}'

concatenatedString = concatenate('I', 'love', 'Programming', 'because', "it's", 'cool')
print(f'Concatenated String: {concatenatedString}')

print('------------------------------------------------------------------------')
print('12. Create a function that returns a string, a float, a boolean, and an integer. Receive those values and print')
print('------------------------------------------------------------------------')
def returnMulipleVals():
    string1 = 'I am here'
    grade = 78.9
    didPass = True 
    age = 40
    return string1, grade, didPass, age

s, g, p, a = returnMulipleVals()
print(f'''
    {s}. My grade is {g} which means I passed, so the rumors are {p}, but I am 
    sad because I am already {a} years old
''')
print()
print('------------------------------------------------------------------------')
print('''
13. Create a function that receives 5 numbers. Mutiply num1 by num2 minus 
num3 divided by num4 plus num5. Return the result. Print the result
''')
print('------------------------------------------------------------------------')

def calculateNumbers(num1, num2, num3, num4, num5):
    result = (num1 * num2 - num3) / (num4 + num5)
    return result

result = calculateNumbers(4, 8, 3, 7, 9)

# 4 * 8 = 32 - 3 = 29
# 29 / 16 = 1.8125, 1.81
print(f'The result of the calculation is {round(result, 2)}')











