# Outline:
# Write a program to find the intersection of two sets. Set1 = {green, blue} Set2 = {blue, yellow}

set1={"green","blue"}
set2={"blue",'yellow'}

intersection_set=set1.intersection(set2)
union_set=set1.union(set2)

print("Set 1 ; ",set1)
print("Set 2 : ",set2)
print("Set after union ; ",union_set)
print("Set after union ; ",set1 | set2)

print("Set after intersection : ",intersection_set)
print("Set after intersection : ",set1 & set2) 

setA={1,2,3}
setB={2,3,4}
diff_set=setA-setB
print("Their difference is : ",diff_set)
print("Their difference is : ",setA.difference(setB)) # Elements that are present in A but not in B

print("Symmetric difference is : ",setA.symmetric_difference(setB)) # Unique elements presnt in set A nsd set B( elements not in both.)

print("Symmetric difference is : ",setA^setB)