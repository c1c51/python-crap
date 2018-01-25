import random
l=["a","b","c","d","e"]
x=0
while x<5:
    l[x]=str(input("name?"))
    x=x+1
y=random.randint(0,4)
print(l[y])
    
