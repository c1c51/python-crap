x=0
l=list()
y=1
z=input("where are you going?")
l.extend([z])
while x==0:
    print("what is your next item on the list")
    z=input()
    l.extend([z])
    y=y+1
    x=int(input("do you want to finish, 1 for yes 0 for no"))
l=" ".join(l)
f=open("29.txt","w")
f.write(l)
f.close()
print("file saved")
