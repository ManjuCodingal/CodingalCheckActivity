# Let's create a function total_calc() that helps us calculate and print out the total amount paid at a restaurant. Given a bill amount and the percentage of the bill amount you decide to pay us a tip (tip_perc ), this function calculates the total amount you should pay.
def calc(bill_amount,tip):
    total=bill_amount+tip
    return total


bill_amount=int(input("Enter your bill amount:"))
tip_perc=int(input("Enter your tip perecntage :"))
tip=bill_amount*tip_perc/100
print("bill amount is : ",bill_amount)
print("The tip is :" , tip)
print("The total amount is :",calc(bill_amount,tip))
