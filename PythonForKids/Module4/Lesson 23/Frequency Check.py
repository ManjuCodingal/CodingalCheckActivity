# Write a program to check the frequency of a value in a dictionary - {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}.
test_dict= {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
X=1
check=0

for i in test_dict:
    if test_dict[i]==X:
        check+=1

print("Frequency : ",check)