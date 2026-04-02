# Write a program to return the country code for various countries. Here’s a dictionary of different country codes - {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}.

country_code={'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}

country=input("Enter Country Name : ")

# print(country_code[country])
print(country_code.get(country,'Not found in dictionary!'))