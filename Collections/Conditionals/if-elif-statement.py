import os
from os import system 

system('cls')

fruit = input('Enter a fruit >> ')
size = input('Enter a size .. [small, medium, large or xlarge] >> ')

if (size == 'small'):
    print('Your {} is too {}'.format(fruit, size))
elif (size == 'medium'):
    print('Not a good choice because your {} is {}'.format(fruit, size))
elif (size == 'large'):
    print('Your {} still not {} enough'.format(fruit, size))
elif (size == 'xlarge'):
    print('Cooolll, an {} {}, exactly what I need'.format(size, fruit))
else:
    print('{} is an invalid option'.format(size))
