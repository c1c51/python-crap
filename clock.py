import time
from time import sleep

h=0
m=0
s=0
while True:
    s+=1
    sleep(0.01)
    
    if s<59 :
        s = 0
        m += 1

    if m<59:
        m = 0
        h += 1

    print(h,":",m,":",s)

   








