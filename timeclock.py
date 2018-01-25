import time
s=0
h=0
m=0
while True:
    for x in range(0, 24):
        for x in range(0, 60):
            for x in range(0, 60):
                print(h,":",m,":",s)
                s=s+1
                time.sleep(0.0001)
            m=m+1
            s=0
        h=h+1
        m=0
    h=0
   


