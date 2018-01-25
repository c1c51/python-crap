s=input("sent")
s=s.lower()
s=s.split()
x=input("what word")
x=x.lower()
y=input("with what")
y=y.lower()
s=[i.replace(x,y) for i in s]
s=" ".join(s)
print(s)
    
