# Program to copy odd lines of one file to another
# open file in read mode
fn = open('FileHandling/FileHandlingp2/file1.txt','r')

# open other file in write mode
fn1 = open('FileHandling/FileHandlingp2/file2.txt', 'w')

# read the content of the file line by line
content = fn.readlines()
# type(cont)


# file 1 content will come in file 2, writing file2 with odd lines in file 1
# Loop through each line using 1-based indexing
for i in range(1, len(content)+1):
	if(i % 2 != 0):  # Check for odd-numbered lines (1st, 3rd, etc.)
		fn1.write(content[i-1])  # i-1 because list indexing starts at 0
	else:
		pass

# close the destinatn file
fn1.close()

# open file in read mode
fn1 = open('FileHandling/FileHandlingp2/file2.txt', 'r')

# read the content of the file
cont1 = fn1.read()

# print the content of the file
print(cont1)

# close all files
fn.close()
fn1.close()