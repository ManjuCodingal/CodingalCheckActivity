# Write a program to generate a random date and time from the given start and end dates

import random
import time

def randomDateGenerator(Start_Date,End_Date):
    print("generating random date between",Start_Date,"and",End_Date)

    randomGenerator=random.random()

    date_format='%m/%d/%Y'

    Start_Time=time.mktime(time.strptime(Start_Date,date_format))
    End_Time=time.mktime(time.strptime(End_Date,date_format))
    randomTime=Start_Time+randomGenerator*(End_Time-Start_Time)
    randomDate=time.strftime(date_format,time.localtime(randomTime))
    return randomDate
print("Random date is ; ",randomDateGenerator('12/1/2019','1/1/2020'))