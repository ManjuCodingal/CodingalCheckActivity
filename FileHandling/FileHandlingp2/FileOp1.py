#open file and read its contents
file = open('FileHandling/FileHandlingp2/file1.txt','r')
print(file.read())
file.close()

#open file and read its beginning 8 characters
file = open('FileHandling/FileHandlingp2/file2.txt','r')
print("\n Read in parts \n")
print(file.read(8))
file.close()

#read first line of file
file = open('FileHandling/FileHandlingp2/file1.txt','r')
print("\n Reading first line...")
print(file.readline())
file.close()

#read first three lines of file
file = open('FileHandling/FileHandlingp2/file1.txt','r')
print("\n Reading multiple lines...")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

#looping through all the lines of the file
file = open('FileHandling/FileHandlingp2/file1.txt','r')
print("\n Looping through the lines...")
for line in file:
  print(line)
file.close()