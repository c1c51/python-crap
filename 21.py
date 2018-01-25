x=float(input("number"))
y=int(input("1 for inch to cm     2 for cms to inch"))
if y==1:
    x=x*2.5400000025908
    print(x,"cm")
else:
    if y==2:
        x=x*0.393700787
        print(x,"inches")
    else:
        print("invalid input")
        

