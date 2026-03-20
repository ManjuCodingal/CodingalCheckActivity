# Define a function to find a cube and define another function which let execute the cube function if the number is divisible by 3
def cube(num):
    return num**3
def cube_cube(num):
    if num%3==0:
        print("cube is ",cube(num))
    else:
        print("The number is not divisible by 3.")
num=int(input("Enter your number : "))
cube_cube(num)