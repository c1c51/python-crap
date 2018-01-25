#Adam Rook 8U Python Assessment BAGELS
import time
import random
from time import sleep
print("Welcome to BAGELS. The computer will pick a random 3 digit number. Your job is to guess it. If you get a correct digit in the right place the game will print green. If you get a correct digit but it is in the wrong place the game shall print amber. If you get a number that isn’t in the number it shall print red. If none of the numbers are correct it will print BAGELS.")
sleep(2)
no1=random.randint(1,9)
no2=random.randint(1,9)
no3=random.randint(1,9)
sleep(0.5)
score=0
guess=0
while score<3:
    print("What is your guess for the first digit?")
    cg1=int(input())
    print("What is your guess for the second digit?")
    cg2=int(input())
    print("What is your guess for the third digit?")
    cg3=int(input())
    if cg1==no1 and cg2==no2 and cg3==no3:
        score=3
        print("BAGELS")
    else:
        if cg1==no1 or cg2==no2 or cg3==no3:
            print("Green")
            score=2
        else:
            if cg1==no2 or cg1==no3 or cg2==no1 or cg2==no3 or cg3==no1 or cg3==no2:
                print("Amber")
                score=1
            else:
                print("Red")
                score=0
                guess=guess+1

print("You won. You did it in",guess,"guesses")
    
