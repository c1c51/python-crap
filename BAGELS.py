#Adam Rook 8U Python Assessment BAGELS
import time
import random
from time import sleep
print("Welcome to BAGELS.")
print("The computer will pick a random 3 digit number.")
print("Your job is to guess it.")
print("If you get a correct digit in the right place the game will print green.")
print("If you get a correct digit but it is in the wrong place the game shall print amber.")
print("If you get a number that isn’t in the number it shall print red.")
print("If none of the numbers are correct it will print BAGELS.")
no1=random.randint(1,9)
no2=random.randint(1,9)
no3=random.randint(1,9)
score=0
guess=0
while score<3:
    print("What is your guess for the first digit?")
    cg1=int(input())
    if cg1==no1:
        print("Green")
        score=2
    elif cg1==no2 or cg1==no3:
        print("Amber")
        score=1
    else:
        print("Red")
        score=0
    print("What is your guess for the second digit?")
    cg2=int(input())
    if cg2==no2:
        print("Green")
        score=2
    elif cg2==no1 or cg2==no3:
        print("Amber")
        score=1
    else:
        print("Red")
        score=0
    print("What is your guess for the third digit?")
    cg3=int(input())
    if cg3==no3:
        print("Green")
        score=2
        guess=guess+1
    elif cg3==no1 or cg3==no2:
        print("Amber")
        score=1
        guess=guess+1
    else: 
        print("Red")
        score=0
        guess=guess+1
    if cg1==no1 and cg2==no2 and cg3==no3:
        score=3
        print("BAGELS")
print("You won. You did it in",guess,"guesses")
name=input("Whats your name?")
f=open("bagels_score.txt","a")
while name in open("bagels_score.txt").read():
    name=input("That name is taken. PLease enter a new one")
print("writing to file")
f.write("\n")
f.write(name)
f.write(":\n")
f.write(str(guess))
f.close()
