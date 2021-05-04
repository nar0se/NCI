import os 
from os import system 
from person import Person

system('cls')

personList = []

carlos = Person('Carlos', 'Martinez', 50, '1234567890')
personList.append(carlos)

yanet = Person()

yanet.setFirstName('Yanet')
yanet.setLastName('Perez')
yanet.setAge(20)
yanet.setPhone('0987654321')
personList.append(yanet)


for person in personList:
    print(f'First Name: {person.getFirstName()}\nLast Name: {person.getLastName()}\nAge: {person.getAge()}\nPhone: {person.getPhone()}')
    print()
