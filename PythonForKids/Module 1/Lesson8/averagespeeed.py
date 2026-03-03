#Three cyclists are riding at the speed of 10,20,30 km/h. find the average and compare which cyclist is riding slower than the average speed?
speed1=10
speed2=20
speed3=30
average_speed=(speed1+speed2+speed3)/3
if speed1<average_speed :
    print("Cyclist 1 is slowr than average speed")
elif speed2<average_speed :
    print("Cyclist 2 is slowr than average speed")
elif speed3<average_speed :
    print("Cyclist 3 is solwer than average speed.")
elif speed1<average_speed and speed2<average_speed :
    print("Cyclist 1 and cyclsit 2 are slower than average speed")
elif speed2<average_speed and speed3<average_speed :
    print("Cyclist 2 and cyclsit 3 are slower than average speed")
elif speed3<average_speed and speed1<average_speed :
    print("Cyclist 3 and cyclsit 1 are slower than average speed")
elif speed1<average_speed and speed2<average_speed and speed3<average_speed :
    print("All three cyclsits are travelling slower than average speed")
else:
    print("two or 3 cyclists are travelling above average speed.")

    
