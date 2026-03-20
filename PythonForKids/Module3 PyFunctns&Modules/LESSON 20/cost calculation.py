# Outline:
# Write a program to calculate the total trip expenditure: Calculate the hotel cost per day Calculate the plane cost Price of the vehicle rented during the trip

def hotel_cost(night):
    return 200*night
def plane_cost(city):
    if city=='Mumbai':
        return 180
    elif city=='udaipur':
        return 170
    elif city=='Lonavala':
        return 175
    
def rental_car_cost(days):
    cost=50*days

    if days>=7:
        cost-=50
    elif days>=2:
        cost-=30

    return cost

def total_cost(city,days,night):
    total=0
    total+=hotel_cost(night)
    total+=plane_cost(city)
    total+=rental_car_cost(days)

    return total
print("Total cost is ", total_cost('Mumbai',5,4))
