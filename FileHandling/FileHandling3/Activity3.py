# Program to eliminate repeated lines from a file

# creating the output file
outputFile = open('UpdatedFile.txt', "w")

# reading the input file
inputFile = open('RepeatedFile.txt', "r")

# holds lines already seen
lines_seen_so_far = set()
print("Eliminating duplicate lines....")
# iterating each line in the file
for line in inputFile:

	# checking if line is unique
	if line not in lines_seen_so_far:

		# write unique lines in output file
		outputFile.write(line)

		# adds unique lines to lines_seen_so_far
		lines_seen_so_far.add(line)		

# closing the file
inputFile.close()
outputFile.close()

# Repeated.txt  : Hey everyone.
# Welcome to Codingal.
# Welcome to Codingal.
# Do you love coding too?
# If yes! then hop on to start your journey of coding with us



# UpdatedFile.txt: Hey everyone.
# Welcome to Codingal.
# Do you love coding too?
# If yes! then hop on to start your journey of coding with us