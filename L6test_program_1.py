# test program
# PMA
# July 2014
# Use this program to practice test plans
import time
print("This program will ask you for a base and a height")
time.sleep(1)
print("It will also ask you for the units")
time.sleep(1)
print("It will then work out the area of a triangle with those measurements")
time.sleep(1)
print("You can enter any lengths bigger than 0, including decimals")
time.sleep(2)
print("Please enter the base:" )
base = int(input())
print("Please enter the height:" )
height = int(input())
if base<=0 or height<=0:
    print("to small")
    quit()
else:
    area=base*height
print("Please enter the units")
units = input()
print("The area is:", area, "square", units)

