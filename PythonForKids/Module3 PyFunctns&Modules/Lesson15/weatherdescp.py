 # Write a program to display the weather in autumn and spring
def weather(season): # defining the function and passing arguements to the function
    if season=="autumn":
        print("The wheather in autumn is cool and dry.")
    elif season=="spring":
        print("The wheather is hot .")
    else:
        print("The whether information for this season is not available.")

season=input("Choose your season :(autumn/spring)")
weather(season) # calling the function.