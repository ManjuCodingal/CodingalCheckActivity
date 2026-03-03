#Customise your ride outline:Write a program to select a ride according to your preference. The ride is divided into two major categories: 1. Bike 2. Car And further, bikes and cars are divided into 2 subcategories. To give the user better selection options.
ride=int(input("Chose your ride as 1 or 2 (1.car/2.bike)") )
if ride==1:
  ride2=int(input("chose your ride from 3 and 4(3.go/4.sedan)"))
  if ride2==3:
    print("Your preferred ride is go car")
  elif ride2==4:
    print("Your preferred ride is sedan car.")
  else :
    print("Wrong choice!")
elif ride==2 :
  ride3=int(input("Chose form 3 and 4 (3.ordinary bike/4.lux bikes)"))
  if ride3==3:
    print("Your preffered ride is ordinary bike )")
  elif ride3==4 :
    print("Your preferred ride is lux bike.")
  else:
    print("Invalid choice!")
else:
  print("Invalid choice!")
