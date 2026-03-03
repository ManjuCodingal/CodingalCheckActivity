#Write a program to check whether the student can take an exam or not. Students will be allowed only in two conditions: If they have a medical cause (‘Y’ for yes and ‘N’ for no). If yes, then they will be allowed. If No, then check attendance If attendance is above 75, then allowed; otherwise, not allow ed.
medical=input("Do you have a medical cause(Y/N) ").upper().strip()
if medical=="Y":#CONDITION 1
    print("You are eligible for exam")
else:
    attendance=int(input("Enter your attendance. :"))
    if attendance>=75:#CONDITION 2
        print("You are allowed")
    else:
        print("You are not eligible.")
