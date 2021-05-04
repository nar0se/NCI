import os 
from os import system
from animal import Animal 

system('cls')

animalList = []

numberOfAnimals = int(input('How many animals do you want to create? >> '))

print(f'Nice!!! {numberOfAnimals} animals!')
print('Here we go!')
typeOfAnimal = input('What is the animal >> ')
print()

for a in range(numberOfAnimals):
#   object   class   
    animal = Animal()
    print(f'----- {str.upper(typeOfAnimal)} # {a + 1} -------')
    breed = str(input(f'What is the breed of your {typeOfAnimal}? >> '))
    animal.setBreed(breed)
    name = str(input(f'What is the name of your {typeOfAnimal}? >> '))
    animal.setName(name)
    size = str(input(f'What is the size of your {typeOfAnimal}? >> '))
    animal.setSize(size)
    age = str(input(f'What is the age of your {typeOfAnimal}? >> '))
    animal.setAge(age)
    temp = str(input(f'What is the temperament of your {typeOfAnimal}? >> '))
    animal.setTemperament(temp)
#   list of objects
    animalList.append(animal)

animalCounter = 1
for animal in animalList:
    print('---------------------------')
    print(f'{typeOfAnimal} # {animalCounter}: ')
    print(f'''
        Breed       ........... {animal.getBreed()}
        Name        ........... {animal.getName()}
        Size        ........... {animal.getSize()}
        Age         ........... {animal.getAge()}
        Temperament ........... {animal.getTemperament()}
    ''')
    animalCounter += 1


    # objects possess properties coming from the class
    # Object <- ...... <- Animal <- (objects)cat, horse, dog