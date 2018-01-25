s=str(input("sent"))
s=s.lower()
s=s.split()
y=0
for x in s:
    if x == "the":
        y=y+1
print(y)
