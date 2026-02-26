# write in file using with()function
# with open('FileOutside.txt', 'w') as file:
#   file.write("Hi! I am Penguin and I am 1 yr old.")
# file.close()

# split file into words
with open('FileOutside.txt', 'r') as file:
  data = file.readlines()
  print("Words in this file are....")
  for line in data:
    word = line.split()
    print (word)
file.close()



# Codingal.txt can be : Codingal is on a mission to inspire school kids to fall in love with coding. 
# Coding helps develop logical thinking and problem-solving skills. 
# Coding jobs are the future. 
# They already constitute more than 60% of all the jobs in Science, Technology, Engineering, and Math. 
# While still in school, those who start young will be ahead of everyone by the time they get into college. 
# They will be creators of the future.
# Do you want to join us too?