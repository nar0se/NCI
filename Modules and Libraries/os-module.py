import os
from os import system, mkdir, listdir, getcwd, getenv, getlogin 

system('cls')

print()
print('************ LIST OF DIRECTORIES AND FILES ***************')
directories = listdir()
print(directories)
print()
print('************ CURRENT WORKING DIRECTORY ***************')
cwd = getcwd()
print(cwd)
print()
print('************ LIST OF DIRECTORIES AND FILES INCLUDING PERMISSIONS ***************')
ListOfDirectoriesAndFiles = system('ls -lah')
print(ListOfDirectoriesAndFiles)
print()
print('************ LOGGED-IN USER ***************')
user = getlogin()
print(user)

print()
print('************ PRINTING THE USER, SHELL, PATH ENVIRONMENT VARIABLES ***************')
user = getenv('USER')
shell = getenv('SHELL')
path = getenv('PATH')
pwd = getenv('PWD')

print(f'USER: {user}, \n\nSHELL: {shell}, \n\nPATH:{path}, \n\nPWD: {pwd}')

# create a folder inside the Modules-and-Libraries directory
mkdir('./Modules-and-Libraries/testFolder')