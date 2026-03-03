#Raj scored 40, 70, 50 and 60 out of 100 in maths, science, Hindi and English. Find the percentage he got?
#Assigning the values
Maths=int(input("Enter maths marks :"))
Science=int(input("Enter maths Science marks :"))
Hindi=int(input("Enter Hindi marks :"))
English=int(input("Enter English marks :"))
#Calculating perecntage
sum=Maths+Science+Hindi+English
Fraction=sum/400
Percentage=Fraction*100
#Printing the percentage
print("Total percentage is ; ",Percentage)