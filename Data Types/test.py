import colorama, os
from os import system
from colorama import Back, Fore

system('cls')
cars = ['BMW', 'Lada', 'Maserati', 'Tesla', 28, True, 34.6]

cars.append('Nissan')

for car in cars:
    print(Fore.MAGENTA, car)

if (4 > 5):
    print('4 is greater than 5')
else:
    print(Fore.RED, '4 is NOT greater than 5')