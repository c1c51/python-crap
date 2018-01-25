import time
from time import sleep
print("H")
h=int(input())
h1=h
x=0
m=0
h=0
while True:
    h1=h
    while x<60:
        print(m,":",h1)
        h1=h1+h
        x=x+1
        sleep(0.1)
    x=0
    m=m+1
    
