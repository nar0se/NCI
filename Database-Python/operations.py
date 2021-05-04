import os 
import sqlOps as sql 
from os import system 
from user import User

system('cls')

users = []
fields = ['First Name', 'Last Name', 'Age', 'Phone'] 

def readUserOperation():
    sql.readUserInfo()

def insertOperation():
    numberOfEntries = int(input('Enter number of records >> '))
    for entry in range(numberOfEntries):
        print(f'--- User # {entry + 1} ---')
        user = User()
        fname = input('What is your first name? >> ')
        user.setFirstName(fname)
        lname = input('What is your last name? >> ')
        user.setLastName(lname)
        age = int(input('What is your age? >> '))
        user.setAge(age)
        phone = input('What is your phone? >> ')
        user.setPhone(phone)
        users.append(user)
        print()
    for user in users:
        sql.insertUserInfo(user.getFirstName(), user.getLastName(), user.getAge(), user.getPhone())

def callUpdateOp(field, index, userId):     
        print(f'Oh, I see that you want to update the {fields[index]}')
        newValue = input(f'What is the new value? >> ')
        sql.updateUser(field, userId, newValue)

def updateOperation():
    sql.readUserInfo()
    userId = int(input('What is the id of the user that you want to update? >> '))
    counter = 1   
    print('These are the fields that you can update:')
    for field in fields: 
        print(f'{counter}. {field}')
        counter += 1
    while True:
        userId = int(input('What is the id of the user that you want to update? >> '))
        field = int(input('Enter the field you want to update [1-4] >> '))
        if (field == 1):
            callUpdateOp('user_firstname', 0, userId)
        elif (field == 2):
            callUpdateOp('user_lastname', 1, userId)
        elif (field == 3):
            callUpdateOp('user_age', 2, userId)
        elif (field == 4):
            callUpdateOp('user_phone', 3, userId)
        else:
            print('Invalid Option')
        extraField = input('Do you want to update another field? [Y/N] >> ')
        if (extraField.upper() == 'N'):
            break

def deleteOperation():
    sql.readUserInfo()
    userId = int(input('which id do you want to delete? >> '))
    sql.deleteUser(userId)