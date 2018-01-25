try:
    colour=input("which colour? - Red Blue Black or White")
    colour=colour.lower()
    if colour=="red" or colour=="black" or colour=="white":
        x=input("pick a number - 1, 2 ,5 or 6")
        if x=="1" or x=="5":
            x=input("pick a number 3,4,7 or 8")
            if x=="3":
                print("you will use python this fortnight")
            elif x=="4":
                print("you will use python this year")
            elif x=="7":
                print("you will use python this millenium")
            elif x=="8":
                print("you will use python today")
            else:
                print("invalid input")
        elif x=="2" or x=="6":
            x=input("pick a number 1,2,5 or 6")
            if x=="1":
                print("you will use python this week")
            elif x=="2":
                print("you will use python this month")
            elif x=="5":
                print("you will use python this decade")
            elif x=="6":
                print("you will use python this century")
            else:
                print("invalid input")
        else:
            print("invalid input")
    
    elif colour=="blue":
        x=input("pick a number - 3, 4 ,7 or 8")
        if x=="8" or x=="4":
            x=input("pick a number 3,4,7 or 8")
            if x=="3":
                print("you will use python this fortnight")
            elif x=="4":
                print("you will use python this year")
            elif x=="7":
                print("you will use python this millenium")
            elif x=="8":
                print("you will use python today")
            else:
                print("invaild input")
        elif x=="3" or x=="7":
            x=input("pick a number 1,2,5 or 6")
            if x=="1":
                print("you will use python this week")
            elif x=="2":
                print("you will use python this month")
            elif x=="5":
                print("you will use python this decade")
            elif x=="6":
                print("you will use python this century")
            else:
                print("invaild input")
        else:
            print("invalid input")
    else:
        print("invalid input")
    
except:
    print("invalid input")
    
    
        
                     
