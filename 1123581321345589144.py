import time
from time import sleep
a=1
no=1/a
print(a)
while True:
    a=a+2
    no=no-1/a
    print(no*4)
    a=a+2
    no=no+1/a
    print(no*4)
