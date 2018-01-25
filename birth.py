#Adam Rook 8U 20/10/15
print("what is your birth month number")
month=int(input())
print("what is your birth day")
day=int(input())
month1=11
day1=3
if month<month1 or month==month1 and day<day1:
    print("it has happened")
elif month==month1 and day==day1 :
    print("it's today")
else:
    print("it hasnt happened")
