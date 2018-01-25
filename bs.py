import time
x=[]
z=0
n=0
i=1
p=0
n=int(input("how many numbers to sort"))
n+=1
while i!=n:
    print("number")
    g=float(input())
    x.append(g)
    i=i+1
while z<(len(x)-1):
    y=0
    while y<(len(x)-1):
        if x[y]>x[y+1]:
            x[y],x[y+1]=x[y+1],x[y]
            y+=1
            print(x)

        else:
            print(x)
            y+=1
        
    z+=1

print("done")
print(x)
            
