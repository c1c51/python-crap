import math
x=0.1
a=999999999999999999999999
while True:
    y=math.sqrt((330*3)/x)
    v=y**2+2*y*x
    x=x+0.1
    if v<a:
        a=v
        print(a)
        print(x)
