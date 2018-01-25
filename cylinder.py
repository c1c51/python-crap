import math
x=0.1
p=3.14159265358979323846264338
a=1000000000000000000000000000000
while True:
    y=math.sqrt(330/(p*x))
    v=2*p*y*x+2*p*y**2
    x=x+0.1
    if v<a:
        a=v
        print(a)
        print(x)
