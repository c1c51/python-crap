#Adam Rook 8U 20/10/2015
import random
print("try to guess my number")
no1 = random.randint(1,6)
print("number")
no=int(input())
if no > no1:
    print("Bigger")
elif no==no1:
    print("thats it well done!!!!")
else:
    print ("lower")
print("the number is ", no1)

    
