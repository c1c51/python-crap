from math import *
y=0
z=9
while True:
    n=int(input("?"))
    print(n)
    y=n
    for x in range (0,100):
        if n<=0:
            print("thats below 0")
        else:
            if n==1:
                print("not prime")
            else:
                x=n/(y-1)
                inNumberint = int(x)
                if x == inNumberint:
                    print ("not prime")6
                else:
                    if y==2:
                        print("prime")
                    else:
                        y=y-1