import time
x=10
y=3628800
while True:
    y=y/x
    x=x-1
    print(y)
    if x==0:
        while True:
            print(time.ctime())
            time.sleep(1)
        
