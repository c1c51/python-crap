while True:
    n=int(input("Give me a number and I will tell you if it is prime or not:"))
    if n>1:
        if n==2:
            print("2 is a prime number")
        else:
            for x in range(2,n):
                if (n % x) == 0:
                    print(n,"isn't a prime number and my evidence is that",n,"=",x,"*",n//x)
                    break
                else:
                    print(n,"is not divisible by",x)
            else:
                print(n,"is a prime number")
    else:
        print(n,"is not a prime number")
