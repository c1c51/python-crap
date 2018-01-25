
y=0
a=[["1+1","324x278","2x2"],[2,90072,4]]
n=str(input("name?"))
x=int(input(a[0][0]))
if x==a[1][0]:
    print("correct")
    y=y+1
else:
    print("incorrect")
x=int(input(a[0][1]))
if x==a[1][1]:
    print("correct")
    y=y+1
else:
    print("incorrect")
x=int(input(a[0][2]))
if x==a[1][2]:
    print("correct")
    y=y+1
else:
    print("incorrect")
f=open("30.txt","a")
f.write(n)
f.write(": \n")
y=str(y)
f.write(y)
f.write("\n")
f.close()
print("well done ",n,". You got ",y," points.")

      
