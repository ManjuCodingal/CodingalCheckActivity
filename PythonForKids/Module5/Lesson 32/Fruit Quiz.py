# Write a program to create a quiz related to multiple fruits using object-oriented programming in Python. Create a class that consists of - 1. a constructor with a dictionary of fruits and respective colours 2. a function to execute the quiz. Here, the fruit will be chosen at random from the dictionary. Then ask the user to enter the colour of that fruit. Evaluate the answer and display the result accordingly.
import random
class FruitQuiz:
    def __init__(self):
        self.fruits={
            "banana":"yellow",
            "apple" :"red",
            "grapes":"green",
            "orange":"orange"
        }
    def quiz(self):
        while True:
            fruit,colour =random.choice(list(self.fruits.items()))
            print("What is the colour of",fruit,"?")
            user_answer=input("Answer: ")

            if user_answer.lower()==colour:
                print("Correct Answer!")
            else:
                print("Incorrect answer")
            option=int(input("Do you wnat to [play again .Press 0 to play agin and 1 to exit(0/1)"))
            if option==1:
                break
obj=FruitQuiz()
obj.quiz()