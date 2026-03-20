# Write a program to check how the exceptions and finally statement works
try:
    num_1,num_2=eval(input("eter your numbers 1,2 :"))
    result=num_1/num_2
    print("The result is : ",result)
except  ZeroDivisionError :
    print("Divission by zero is error !")
except SyntaxError:
    print("Invalid syntax!")
except ValueError:
    print("Pls input a number .")
except :
    print("Wrong Input ! ")
else:
    print("No exception")
finally:
    print("The program is over ! ")
     