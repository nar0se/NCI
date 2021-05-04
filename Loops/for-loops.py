import os 
from os import system
system('cls')
from colorama import Fore


counter_i = 0
counter_j = 0
counter_x = 0
counter_y = 0

# Nested For loops
for i in range(1, 11): # OUTER LOOP -> loops 10 times
    print()
    print(Fore.RED, f'i ................... {i}')
    counter_i += 1
    for j in range(1, 6): # INNER LOOP -> loops 50 times
        print(Fore.YELLOW, f'j ................ {j}')
        counter_j += 1
        for x in range(1, 4): # INNER LOOP -> loops 150 times
            print(Fore.BLUE, f'x ............. {x}')
            counter_x += 1
            for y in range(1, 3): # INNER LOOP -> loops 300 times
                print(Fore.GREEN, f'y .......... {y}')
                counter_y += 1

# First iteration
    # i loops first time (1)
        # j loops the first time (1)
            # x loops the first time (1)
                # y loops 2 times
            # x loops for the second time (2)
                # y loops 2 times
            # x loops for the third time (3)
                # y loops 2 times
        # j loops for the second time (2)
            # x loops the first time (1)
                # y loops 2 times
            # x loops for the second time (2)
                # y loops 2 times
            # x loops for the third time (3)
                # y loops 2 times

print(Fore.MAGENTA)
counterList = []
print('Counter i => ', counter_i)
counterList.append(counter_i)
print('Counter j => ', counter_j)
counterList.append(counter_j)
print('Counter x => ', counter_x)
counterList.append(counter_x)
print('Counter y => ', counter_y)
counterList.append(counter_y)
print(Fore.CYAN, 'Total loops: {}'.format(sum(counterList)))

counter_z = 0
counter_w = 0

print()
print('---------------------------')
for z in range(1, 20):
    print(Fore.RED, f'z ........... {z}')
    counter_z +=1 
    for w in range(1, 10):
        print(Fore.BLUE, f'w ......... {w}')
        counter_w +=1 

print()
print(Fore.YELLOW)
print(f'Counter Z: {counter_z}')
print(f'Counter W: {counter_w}')
print(Fore.GREEN)
print('Total loops: {}'.format(counter_z + counter_w))

# counter_z = 1, counter_w = 9