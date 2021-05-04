import os
from os import system
from colorama import Fore, Back, Style

system('cls')

# Consider the following tuples:
# PLEASE USE A FOR LOOP
# ​
# 1. Add all the numbers in them using a for loop
# The total is 846

tuple1 = (23, 45, 12, 56, 78, 34, 12, 78, 89) # -> 424
tuple2 = (27, 39, 18, 50, 75, 33, 17, 70, 90) # -> 419​

addition1=0
for num in range(len(tuple1)): #assuming both the tuples have equal lengths
    addition1 += tuple1[num] + tuple2[num]
print(addition1)
print('----------------------------------------')

# 2. Find the total of all the even numbers in the tuples (all combined)

sumeven=0
sumodd=0
for num in range(len(tuple1)): #assuming both the tuples have equal lengths
    if(tuple1[num] %2 == 0):
        sumeven += tuple1[num] 
    else:
        sumodd += tuple1[num]
    if(tuple2[num] %2 == 0):    
        sumeven += tuple2[num]
    else:
        sumodd += tuple2[num]
print(sumeven,sumodd)
print('----------------------------------------')

# 3. Find the total of all the odd numbers in the tuple (all combined)

sumeven=0
sumodd=0
for num in range(len(tuple1)): #assuming both the tuples have equal lengths
    if(tuple1[num] %2 == 0):
        sumeven += tuple1[num] 
    else:
        sumodd += tuple1[num]
    if(tuple2[num] %2 == 0):    
        sumeven += tuple2[num]
    else:
        sumodd += tuple2[num]
print(sumeven,sumodd)
print('----------------------------------------')

# 4. In a for loop, accomplish the following
# - Initialize an empty list
# - The list is a list of dictionaries -> [Each dictionary is a person]
# - Have the user enter how many dictionaries he or she wants to add to the list
# - Each dictionary must contain the following
#    # first name
#    # last name
#    # age
#    # phone
#    # address 1
#    # address 2
#    # city
#    # state
#    # zip code
# - Print the list of dictionaries

newList = []
newPersonalDictionary = {}
numberOfPeople = int(input('How many people do you want to add to my list? >> '))
counter = 1

for index in range(numberOfPeople):
    print(f'Person # {counter}: ')
    fname = input('Enter your first name >> ')
    lname = input('Enter your last name >> ')
    age = int(input('Enter age >> '))
    phone = int(input('Enter your phone number >> '))
    addr1 = input('Enter address line one >> ')
    addr2 = input('Enter address line two >> ')
    city = input('Enter your city >> ')
    state = input('Enter your state >> ')
    zipc = int(input('Enter your zipcode >> '))
    
    newPersonalDictionary['fname'] = fname
    newPersonalDictionary['lname'] = lname
    newPersonalDictionary['age'] = age
    newPersonalDictionary['phone'] = phone
    newPersonalDictionary['addr1'] = addr1
    newPersonalDictionary['addr2'] = addr2
    newPersonalDictionary['city'] = city
    newPersonalDictionary['state'] = state
    newPersonalDictionary['zipc'] = zipc
    newList.append(newPersonalDictionary)
    counter+=1

# 5. Outside the loop, append one more person dictionary to the list above

newPerson = {}
newPerson['fname'] = 'Sam'
newPerson['lname'] = 'Boye'
newPerson['age'] = '33'
newPerson['phone'] = '804-333-3333'
newPerson['addr1'] = '201 One Hundred St'
newPerson['addr2'] = 'Apt 201'
newPerson['city'] = 'Fredericksburg'
newPerson['state'] = 'VA'
newPerson['zipc'] = '24444'
newList.append(newPerson)

dictionaryCounter = 1
# nested for loop
for dictionary in newList:
    print()
    print('------------------------------')
    print(f'---- Dictionary # {dictionaryCounter} ----')
    for key, value in dictionary.items():
        print(f"'{key}': {value}")
    dictionaryCounter += 1
print('-------------------------------')

# 6. BONUS:
#     - Create a program that prompts users to select reservation packages 
#       [Bronze, Silver, and Gold] with their respective prices
#     - If Bronze is chosen, there is a bonus of $200
#     - If Silver is chosen, there is a bonus of $400
#     - If Gold is chosen, there is a bonus of $600
#     - Calculate subtotal, taxes, and grand total
#     - Display order details [colorama preferred]


#     - Use for loops seen in class, functions, and lists
# reservation_dict={"Bronze": "300",
#                   "Silver": "600",
#                   "Gold": "900" }
# bonus_dict={"Bronze": "200",
#                   "Silver": "400",
#                   "Gold": "600" }


# selected_package=input("Select a package Bronze/Silver/Gold >> ")

# subtotal=int(reservation_dict[selected_package]) + int(bonus_dict[selected_package])
# print('-------------------------------')
# print("Your Subtotal: $" +str(subtotal))
# print('-------------------------------')
# tax=subtotal * 0.06
# grandtotal=subtotal + tax
# print(Style.RESET_ALL)
# print(Fore.RED)
# print('-------------------------------')
# print("Your Grand Total with 6% tax: $" +str(grandtotal))
# print('-------------------------------')
# print(Style.RESET_ALL)

reservation_packages={"Bronze": [300,200], "Silver": [600,400], "Gold": [900,600]}

selected_package=input("Select a package Bronze/Silver/Gold >> ")

mypricelist=reservation_packages[selected_package]
subtotal=0
for value in mypricelist:
    subtotal += value
print('-------------------------------')
print("Your Subtotal: $" +str(subtotal))
print('-------------------------------')
tax=subtotal * 0.06
grandtotal=subtotal + tax
print(Style.RESET_ALL)
print(Fore.RED)
print('-------------------------------')
print("Your Grand Total with 6% tax: $" +str(grandtotal))
print('-------------------------------')
print(Style.RESET_ALL)

system('clear')
packagesList = ['Bronze', 'Silver', 'Gold']
packagesPricesList = [15999.99, 18999.99, 20999.99]
counter = 1
BONUS = 0
packageTotalPrice = 0

def calculatePackagePrice(packagePrice, bonus, package):
    print()
    print(Fore.YELLOW, f'You have selected the {package} package')
    print()
    total = 0
    taxes = packagePrice * 0.07
    subTotal = packagePrice 
    total = subTotal + taxes - bonus 
    print(Fore.RED, '               ---- ORDER SUMMARY ----')
    print(Fore.MAGENTA, f'''
         Package:...................   {package} 
         Cost:...................... $ {packagePrice}
         Subtotal:.................. $ {subTotal}
         Taxes:..................... $ {round(taxes, 2)}    
         Bonus:..................... - $ {bonus}        
         GrandTotal:................ $ {round(total, 2)}
''')

# Professor's Answer

print('---- AVAILABLE PACKAGES ----')
for index in range(len(packagesList)):
    print(f'{counter}. {packagesList[index]} -> ${packagesPricesList[index]}')
    counter += 1

while True:
    while True:
        selection = int(input('Enter an option above [1-3] >> '))
        if (selection == 1):
            BONUS = 200
            calculatePackagePrice(packagesPricesList[0], BONUS, 'Bronze')
            break
        elif (selection == 2):
            BONUS = 400
            calculatePackagePrice(packagesPricesList[1], BONUS, 'Silver')
            break
        elif (selection == 3):
            BONUS = 600
            calculatePackagePrice(packagesPricesList[2], BONUS, 'Gold')
            break
        else:
            print('invalid option')
    print(Style.RESET_ALL)
    choice = input('Do you want to purchase another package? [ Y/N ] >> ')  
    if (choice.upper() == "N"): 
        print('Thanks for using our services')
        break
