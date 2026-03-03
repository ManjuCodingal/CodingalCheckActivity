amount=int(input("Enter your amount : "))
#Calculating no of notes
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10
print("Count of notes of 100 rupee is : ",note1)
print("Count of notes of 50 rupee is : ",note2)
print("The count of notes of 10 rupees is : ",note3)