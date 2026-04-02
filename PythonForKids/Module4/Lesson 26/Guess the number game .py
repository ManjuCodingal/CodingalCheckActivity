# 1) Import the required modules:
#    a) Import `random` to generate a random number.
#    b) Import `time` to add delays using `sleep()`.
import random
import time

# 2) Generate a random integer between 1 and 100 using `random.randint(1, 100)`
#    and store it in `number`.
#    (This will be the secret number to guess.)
number=random.randint(1,100)

# 3) Define a function `intro()` to introduce the game:
def intro():
#    a) Ask the user for their name.
    global name
#    b) Declare `name` as a global variable so it can be used outside the function.
#    c) Take the input and store it in `name`.
    print("what is your name?")
    name=input()
#    d) Print a welcome message and tell the user the number is between 1 and 100.
    print("the computer is thinking about a number between 1 to 100!")
#    e) Check if the secret `number` is even or odd using `% 2`:
#       - If even, set `x = 'even'`
#       - Else, set `x = 'odd'`
    if number%2==0:
        x='even'
    else:
        x='odd'
#    f) Print whether the secret number is even or odd.
    print("The number is ",x,'.')
#    g) Add small delays using `time.sleep()` and then ask the user to start guessing.
    time.sleep(1)
    print("Please guess the number !")

# 4) Define a function `pick()` that runs the guessing process:
def pick():
    guessesTaken=0 #    a) Initialize `guessesTaken = 0` to count how many guesses the player makes.

        

# 5) Use a `while` loop that runs until the user has taken 6 guesses:
#    a) Add a small delay using `time.sleep(.25)`.
#    b) Ask the user to enter a guess and store it in `enter`.
    while guessesTaken<6:
        time.sleep(0.25)
        enter=input("Enter your guess : ")

# 6) Validate the guess using a `try` block:
#    a) Convert `enter` into an integer and store it in `guess`.
#    b) Check if `guess` is within the range 1 to 100.
        try:
            guess=int(enter)
            if 1<=guess<=100:
                guessesTaken=guessesTaken+1 # 7) If the guess is in range (1 to 100):
#    a) Increase `guessesTaken` by 1.


#    b) If `guessesTaken < 6`, compare the guess with the secret number:
#       i) If `guess < number`, print "too low".
#       ii) If `guess > number`, print "too high".
#       iii) If `guess != number`, print "Try Again!" after a short delay.
#       iv) If `guess == number`, stop the loop using `break`.
                if  guessesTaken<6:
                    if guess<number:
                        print("too low")
                    elif guess>number:
                        print("Too high")
                    else:
                        print("Correct number !")
                        print("congratulations!",name,"You guessed the number ",number,"in ",guessesTaken,"attempts!")
                        break


# 8) If the guess is out of range:
#    a) Print a message saying the number is not in range.
#    b) Ask the user again to enter a number between 1 and 100.

            if guess>100 or guess<1:
                print("Not in range !Enter the number in the range !")
                
# 9) Use an `except` block to handle invalid input (non-numeric):
#    a) Print a message saying the entered value is not a number.
        except:
            print("Invalid number!")

# 10) After the guessing loop ends:
#     a) If `guess == number`, print a success message with the user's name
#        and the number of guesses taken.
#     b) If `guess != number`, print the correct secret number.
    if guess!=number:
        print("The number computer was thinking was ",number)
     

# 11) Create a variable `playagain = "yes"` to start the game loop.
playagain="yes"


# 12) Use a `while` loop to allow replaying the game:
#     a) Repeat while `playagain` is "yes", "y", or "Yes".
#     b) Call `intro()` to show game introduction.
#     c) Call `pick()` to run the guessing game.
#     d) Ask the user if they want to play again and store the response in `playagain`.
while playagain.lower() == "yes":
    number=random.randint(1,100)
    intro()
    pick()
    playagain=input("Do you want to play again !(yes/no) : ")