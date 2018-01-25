print("choice")
c=str(input())
p=0
pcp=0
import random
c=c.upper()
pc=random.choice("ROCK,PAPER,SCISSORS")
for x in range(0, 3):
    if c==pc:
        print("draw")
    if c=="ROCK" and pc=="SCISSORS" or c=="PAPER" and pc=="ROCK" or c=="SCISSORS" and pc=="PAPER":
        print("you win")
        p=p+1
    if c=="ROCK" and pc=="PAPER" or c=="PAPER" and pc=="SCISSORS" or c=="SCISSORS" and pc=="ROCK":
        print("lose")
        pcp=pcp+1
        
    
