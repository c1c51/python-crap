from math import *
y=0
z=9
while True:
    n=int(input("?"))
    print(n)
    y=n
    for i in range (0,y-1):
        if n<=0:
            print("thats below 0")
        else:
            if n==1:
                print("not prime")
            else:
                x=n/(y-1)
                inNumberint = int(x)
                if x == inNumberint:
                    print ("not prime")
                    y=y-1
                else:
                    print("prime")
