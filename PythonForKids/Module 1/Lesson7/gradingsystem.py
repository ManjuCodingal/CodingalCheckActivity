#Write a program to show students' grades by entering five subject marks and calculating average marks and grades. For example, if the average is between 91 to 100, A2 is between 81 to 90, and so on, do it till grade E2
mark1=int(input("Enter marks 1 "))
mark2=int(input("Enter marks 2 "))
mark3=int(input("Enter marks 3 "))
mark4=int(input("Enter marks 4 "))
mark5=int(input("Enter marks 5 "))
average=(mark1+mark2+mark3+mark4+mark5)/5
print("The average is ",average)
if average>91 and average<=100 :
    print("Your grade is A1")
elif average>=81 and average<91 :
    print("Your grade is A2")
elif average>=71 and average<81 :
    print("Your grade is B1")
elif average>=61 and average<71 :
    print("Your grade is B2")
elif average>=51 and average<61 :
    print("Your grade is C1")
elif average>=41 and average<51 :
    print("Your grade is C2")
elif average>=31 and average<41 :
    print("Your grade is D")
elif average>=21 and average<31 :
    print("Your grade is E1")
elif average>=0 and average<21:
    print("Your grade is E2")
else:
    print("Invalid input!")