hprime=2
n=95
while True:
   for p in range(0,99999999999999999999): 
        print(hprime)
        for x in range(2,n):
                if (n % x) == 0:
                    n=n+1
                    break
                else:
                      hprime=n
                      n=n+1


