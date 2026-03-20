def calculate_due(bill_amount, paid_amount):
    
    due = bill_amount - paid_amount
    
    return due


# Taking input from user
bill = float(input("Enter the bill amount: "))
paid = float(input("Enter the amount paid by the customer: "))

# Calling the function
due_amount = calculate_due(bill, paid)

print("Customer Due Amount:", due_amount)