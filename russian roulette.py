import random
import time
bullet=random.randint(1,6)
x=1
print("Welcome to Russian Roulette")
time.sleep(1)
print("spinning the cylinder")
while x<random.randint(15,30):
    time.sleep(0.1)
    print("click")
    x=x+1
shot=random.randint(1,6)
if shot=bullet:
    print("i'm sorry")
    while True:
        os.system("lol")
