pb=q=y=s=0
quiz=[["Who won the 2016 male downhill mountain biking world championships?","Who won the 2016 female downhill mountain biking world championships?","Who is the famous mountain biker famous for his films such as Wee day out and The ridge?","How many times has Julien Absalon won the xc world championships?","Which is the longest track on the 2017 dh world cup circuit"],["A: Greg Minnaar B: Danny Hart C: Aaron Gwin","A:Rachel Atherton B:Tahnee Seagrave C:Manon Carpenter","A:Hans Ray B:Danny Macaskill C:Ali Clarkson","A:4 B:3 C:5","A:Lourds B:Cairns C:Fort William"],["B","A","B","C","C"],["A","B","C","D"]]
name=input("what is your name?")
print("Hello",name,". Welcome to the MTB quiz")
def question():
    global s,y,q
    while y==0:
        print(quiz[0][q])
        a=input(quiz[1][q])
        a=a.upper()
        if a in quiz[3]:
            y=1
            if a==quiz[2][q]: print("correct"); s+=1; q+=1
            else: print("incorrect"); q+=1    
        else: print("invalid input; try again")    
    y=0
while y==0:
    q=s=y=x=0
    if pb!=0: print("Your best this game is",pb)
    question()
    question()
    question()
    question()
    question()
    if s>pb: pb=s
    if s>0: print("Well done", name,", you scored ",s)
    else: print("Well",name,"you failed with a grand total of",s,"points.")    
    if s>3:
        while x<5: print("Well done"); x=x+1
    y=int(input("Do you want to play again? 0 for yes; 1 for no"))
y=int(input("Would you like to save your score? 1 for yes; 0 for no"))
if y==1: f=open("score.txt","a"); f.write(name); f.write(":\n"); pb=str(pb); f.write(pb); f.write("\n"); f.close(); print("score saved to \\\SAN\Pupils\2014\14urooka\My Documents\Yr 9\ICT\Python\Assessment\score.txt")
