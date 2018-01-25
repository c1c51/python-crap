#The program asks the user what year they are in at school and then tells them whether they are in primary school, KS3, KS4 or have finished their GCSEs
year = int(input("what year are you in at school?"))
if year <= 6:
    print ("You are in primary school")
elif year <=9:
    print ("You are in KS3")
elif year <=11:
    print("you're in KS4")
else:
    print("Lucky you, you've finished your GCSEs")
