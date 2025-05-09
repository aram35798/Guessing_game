#Guessing Game
import random
while True:
    User=(input("Pick a number between 1-10: "))
    print ("Your guess is: " + User)
    Number = random.randint(1,10)

    if Number == User:
        print("That's right, the number was" + Number)
        break
    else:
        print("Wrong, I was thinking about" + str(Number))

    #If the statement is true then it will print "right"
    # But if statement is wrong then it should stop the loop