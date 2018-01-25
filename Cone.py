import math
x=0.1
p=3.14159265358979323846264338
a=999999999999999999999999
while True:
    y=math.sqrt(3((330/p)/x))
    t=math.sqrt(y**2+x**2)
    v=p*y(y+t)
    x=x+0.1
    if v<a:
        a=v
        print(a)
        print(x)
