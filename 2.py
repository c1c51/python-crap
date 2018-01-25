#It asks the user what the temperature is and depending on the value that the user inputs shall tell the user whether it is too cold, too hot or just right
temperature = int(input("Whats is the temperature?"))
if temperature < 10:
    print ("Brr... It's too cold!")
elif temperature > 25:
    print ("It's too hot!")
else:
    print ("It's just right!")
