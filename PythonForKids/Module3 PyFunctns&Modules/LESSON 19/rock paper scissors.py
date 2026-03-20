# Create a program to play rock, paper, and scissors. Use a random module to select from the given options Check whether the random guess matches the user’s answer

import random

while True :
    user_action=input("Enter you choice (rock/paper/scissors)").lower()

    all_actions=["rock","papaer",'scissors']

    computer_action=random.choice(all_actions)

    print("You chose",user_action,"Computer chose",computer_action)

    if user_action not in all_actions :
        print("Invalid choice!")
    elif user_action==computer_action:
        print ("its a tie!!")
    elif user_action=="rock":
        if computer_action=="scissors":
            print("You won ! ")
        else:
            print("Computer wins !")
    elif user_action=="paper":
        if computer_action=="rock":
            print("you won !")
        else:
            print("Computer won")
    else:
        if computer_action=="rock":
            print("Computer wins !")
        else:
            print("You won !")
    play_again=input("Do you want to playagain(yes/no)")
    if play_again !="yes":
        break
    