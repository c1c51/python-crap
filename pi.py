import time
import os
a=1
no=4/a
print(a)
while True:
    a=a+2
    no=no-4/a
    print("TAU=",no*2)
    a=a+2
    no=no+4/a
    print("pi=",no)
    os.system(clear)
    
