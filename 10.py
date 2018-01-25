import random
import time
from time import sleep
c=0
print("just hit enter...")
code=str(input())
for x in range(0, 3):
    b=random.choice(['rock','paper','scissors'])
    print("your choice")
    a=str(input())
    if a==b:
        print("draw")
        print("computer played ",b)
    if a=='rock' and b=='paper' or a=='paper' and b=='scissors' or a=='scissors' and b=='rock':
        print("lose")
        c=c-1
        print("computer played ",b)
    if a=='rock' and b=='scissors' or a=='paper' and b=='rock' or a=='scissors' and b=='paper':
        print("win")
        c=c+1
        print("computer played ",b)
print("you scored", c)
if c>=1:
    d='win'
elif c==0:
    d='draw'
elif c<=0:
    d='lose'
    print("therefor you", d)
