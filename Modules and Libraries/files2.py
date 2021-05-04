import os, time 
from os import system
from time import sleep 
from colorama import Fore

system('cls')

sleep(2)
print('Good bye!')

fileName = input('What do you want to name your file? >> ')
extension = input('What extension do you want to use? (e.g., pdf, txt, py, ds, js, ...) >> ')
content = input('What content do you want to add to the file? >> ')
file = fileName + '.' + extension
path = f'./Modules-and-Libraries/{file}'

system(f'touch {path}')
system(f"echo '{content}' > {path}")


# this will read the content of the new file
f = open(path, 'r')
fileContent = f.read()
system('clear')
print(f'We are printing the content of {file}....')
sleep(3)
print()
print(Fore.RED, fileContent)
f.close()