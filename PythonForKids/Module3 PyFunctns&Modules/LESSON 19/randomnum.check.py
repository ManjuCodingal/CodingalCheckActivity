# Write a program to generate a random integer and match it with the input given by the user?
import random

play=True

number=str(random.randint(0,9)) # str to convert number gen by computer to a string so that we can comparison as in line 16

print("Guess Game")
print("I have generated a random number from1 to 9")
print("Guess it !")

while play:

    guess=input("Enter your guessed number : ")

    if number==guess:
        print("You won the game ! Your number was right !!")
        break
    else:
        print("Your guess was wrong ! Try again ")