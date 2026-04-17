# Create a python program to create a flashcard using object-oriented programming. A flashcard is a two-sided card with information on both sides that can assist memory. A question and an answer are usually printed on one side of a flashcard. Follow these steps to complete the activity - 1. From the user, take the input for a word and its definition. 2. To assign values for Word and Meaning, create a class called flashcard and use the __init__() function. 3. We'll use the __str__() function to get a string with the term and its definition. 4. Save the strings that have been returned in a list. 5. To print all of the stored flashcards, use a while loop.
class flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word + "("+self.meaning+")"
flash=[]
while True:
    word=input("Enter a word : ")
    meaning=input("Enter menaing")
    flash.append(flashcard(word, meaning))
    option=int(input("Add one more .Enter 0 to add another and 1 to exit (0/1): "))
    if option==1:
        break
print("Flashcard")

for i in flash:
    print("--",i)