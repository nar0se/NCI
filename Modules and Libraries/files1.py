import os 
from os import system

system('cls')

path = './Modules-and-Libraries/newFile.txt'

with open (path, 'w') as file:
    file.write('I am learning to use files')
    file.close()


while True:
    content = input('What content do you want to add to the file? >> ')
    with open(path, 'a') as file:
        file.write(f'\n{content}')
        file.close()
    response = input('Do you want to add more content [Y/N]? >> ')
    if(str.upper(response) == 'N'):
        break