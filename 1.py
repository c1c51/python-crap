#It asks the user what the temperature is and depending on the value shall decide if the user will need a coat or not
temperature = int(input("what is the temperature?"))
if temperature < 12:
    print ("You should wear a coat")
else:
    print ("No need for a coat today!")
