# Write a program to check the current date and time?

import datetime

current_datetime=datetime.datetime.now()

print("Current date and time is : ",current_datetime)
print("Current time is ; ",current_datetime.time())
print("Current date is : ",current_datetime.date())
print("Current yaer is :",current_datetime.date().today().year)
print("the current month is ",current_datetime.date().today().month)