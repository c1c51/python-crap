import time
from time import sleep
print("how long")
time=int(input())
print(time)
x = 1
time1=0
while True:
    time1=time1+3
    print(time1)
    if time1==time:
        print("thats it")
        sleep(1)
        quit()
    sleep(0.1)
