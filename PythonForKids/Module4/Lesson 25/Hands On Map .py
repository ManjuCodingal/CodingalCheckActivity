# Write a program to return the addition of numbers of two different lists. Then, display a list that is square of numbers of another list. Use the map() function here to get the desired result.
numbers1=[1,2,3,4,5]
numbers2=[10,20,30,40,50]

result=map(lambda x,y:x+y,numbers1,numbers2) # lambda x,y : x+y is used to define anonymous function which takes 2 prameters(x,y) and it will return their sum.
print('Addition of two lists is ',list(result))

new_list=[1,5,6,9,3]
def square(n):
    return n**2
square=list(map(square,new_list))
print("Square of numbers in the list is  ",square)
