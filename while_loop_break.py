# while loop with break
# PMA
# July 2014
# shows a different while loop

# The program will wait until the user enters a number bigger than 10

while True:
    print("Please enter a number bigger than 10:", end=" ")
    number = int(input())

    if number > 10:
        break

