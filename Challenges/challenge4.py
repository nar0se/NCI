import os
from os import system
from colorama import Fore, Back, Style
from math import ceil
from time import sleep

system('cls')


# Assume that a gallon of paint covers about 350 square feet of wall space. 
# Create an application that prompts the user for the length, width, and height of a rectangular room. 
# Pass these three values to a function that does the following:
#   - Calculates the wall area for a room.
#   - Passes the calculated wall area to another method that calculates and returns the number of gallons of paint needed.
#   - Displays the number of gallons needed.
#   - Computes the price based on a paint price of $32 per gallon, assuming that the painter can buy any fraction of a gallon of paint 
#     at the same price as a whole gallon.
#   - Returns the price
# ​
# The final price is displayed. For example, the cost to paint a 15-by-20-foot room with 10-foot ceilings is $64. 
# Save the application as paintcalculator.py

# 350 = 20 * 17.5

length = float(input('Enter the length of the room >> '))
width = float(input('Enter the width of the room >> '))
height = float(input('Enter the height of the room >> '))

def roomarea(length, width, height):
    area=2 * ((length * height) + (width * height))
    return area
print(f'')

area1=roomarea(length, width, height)
area = round(area1,2)
print(f'Your total square footage of your room is {area}')

def paint123(area):
    paint = area / 350
    return paint

paint1 = paint123(area)
paint = round(paint1,2)
print(f'Your room will need {paint} gallons of paint')


def cost(paint):
    paint1=ceil(paint)
    costprice = paint1 * 32
    return costprice

costprice = cost(paint)

print(f'The cost to paint a {length}-by-{width}-foot room with {height}-foot ceilings is ${costprice}')

# Professor's Answer

import os 
from os import system
import math
from math import ceil

system('clear')
gallonPrice = 32
fname = input('Enter your first name so that I can address you properly >> ')
print(f'{fname}, great!! Let us grab some info on your wall!!')

def calculateGallons(a):
    numOfGallons = a/350
    return numOfGallons

def calculatePrice(l, w, h):
    area = 2 * l * (l + w)
    gallons = calculateGallons(area)
    priceToPaintWall = ceil(gallons) * gallonPrice
    return priceToPaintWall


length = float(input('Enter the length >> '))
width = float(input('Enter the width >> '))
height = float(input('Enter the height >> '))
price = calculatePrice(length, width, height)

print(f'The price to paint a {length} x {width} x {height} wall is ${price} dollars')