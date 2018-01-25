#NEVER EVER EVER MAKE INVALID INPUT
#I'M WARNING YOU
import os
import time
try:
    colour=input("which colour? - Red Blue Black or White")
    colour=colour.lower()
    if colour=="red" or colour=="black" or colour=="white":
        num1=input("pick a number - 1, 2 ,5 or 6")
        if num1=="1" or num1=="5":
            num2=input("pick a number 3,4,7 or 8")
            if num2=="3":
                print("you will use python this fortnight")
            elif num2=="4":
                print("you will use python this year")
            elif num2=="7":
                print("you will use python this millenium")
            elif num2=="8":
                print("you will use python today")
            else:
                print("invaild input")
                time.sleep(1)
                print("i'm sorry")
                while True:
                    os.system("lol")
        if num1=="2" or num1=="6":
            num3=input("pick a number 1,2,5 or 6")
            if num3=="1":
                print("you will use python this week")
            elif num3=="2":
                print("you will use python this month")
            elif num3=="5":
                print("you will use python this decade")
            elif num3=="6":
                print("you will use python this century")
            else:
                print("invaild input")
                time.sleep(1)
                print("i'm sorry")
                while True:
                    os.system("lol")
    if colour=="blue":
        num1=input("pick a number - 3, 4 ,7 or 8")
        if num1=="8" or num1=="4":
            num4=input("pick a number 3,4,7 or 8")
            if num4=="3":
                print("you will use python this fortnight")
            elif num4=="4":
                print("you will use python this year")
            elif num4=="7":
                print("you will use python this millenium")
            elif num4=="8":
                print("you will use python today")
            else:
                print("invaild input")
                time.sleep(1)
                print("i'm sorry")
                while True:
                    os.system("lol")
        if num1=="3" or num1=="7":
            num3=input("pick a number 1,2,5 or 6")
            if num3=="1":
                print("you will use python this week")
            elif num3=="2":
                print("you will use python this month")
            elif num3=="5":
                print("you will use python this decade")
            elif num3=="6":
                print("you will use python this century")
            else:
                print("invaild input")
                time.sleep(1)
                print("i'm sorry")
                while True:
                    os.system("lol")
except:
    print("invalid input")
    time.sleep(1)
    print("i'm sorry")
    while True:
        os.system("lol")
                     
