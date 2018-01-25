from tkinter import *
start=Tk()
def correct():
    global buttona
    buttona.pack_forget()
    text=Label(start,text="correct")
    text.pack()
    buttona=Button(start,text="correct")
    buttona.pack()
def test():
    global button2
    button2.pack_forget()
    text.pack_forget()
    button2=Button(start,text="continue",command=test)
    buttona=Button(start,text="A: 2",command=correct)
    buttona.pack()
button2=Button(start,text="continue",command=test)


text=Label(start,text="Hello, Welcome to my quiz")
text.pack()
button2=Button(start,text="continue",command=test)
button2.pack()





#awnser=input()
#if awnser=="A":
#    print("correct")
#elif awnser=="B" or awnser=="C":
#   print("incorrect")
    
