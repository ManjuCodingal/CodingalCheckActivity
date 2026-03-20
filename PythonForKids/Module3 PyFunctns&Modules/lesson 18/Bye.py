# Write a program using nested while loop. If the value is divided by two, then it will run an infinite loop of the bye.
valid=False
while not valid :
    try:
        num=int(input("Enter Your Number : "))
        while num%2==0:
              print("Bye")
        valid=True
    except ValueError :
        print("ValueError")

# Output 
    
    # Case 1:
    #       num=4,prints "bye" Infinitely.

    # Case 2:
    #       num=5: Loop ends 

    # Case 3:
    #       num=letters , number with spaces , any valueeroor : ValueError ..Loop continues.


