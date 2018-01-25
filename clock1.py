import time
from time import sleep
h=0
m=0
s=0
while True:
    while h<24:
        while m<60:
            while s/60:
                print(h,":",m,":",s)
                s=s+1
                sleep(0.01)
            m=m+1
        h=h+1
    h=0
    m=0
    s=0

