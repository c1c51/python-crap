y=1
n=str(input("name?"))
x=int(input("what is 1+1?"))
if x==2 or x==11:
    print("correct")
    y==y+1
else:
    print("incorrect")
x=int(input("what is 324x278?"))
if x==90072:
    print("correct")
    y=y+1
else:
    print("incorrect")
x=float(input("what is 42546874+542458785/572472723?"))
if x==42546874.94757141:
    print("correct")
    y=y+1
else:
    print("incorrect")
print("well done ",n,". You got ",y," points.")
f=open("26.txt","w")
f.write(n)
f.write(": \n")
y=str(y)
f.write(y)
f.write("\n")
f.close()
