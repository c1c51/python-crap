import time
import random
import math
while True:
    n=int(input("Think of a cardinal between 1 and 19"))
    print(n)
    if n<0:
        print("thats below 0")
    else:
        if n==1:
            print("not prime")
        else:
            x=((math.factorial(n-1))+1)/n
            inNumberint = int(x)
            if x==inNumberint:
                print ("prime")
            else:
                print ("not prime")
            




