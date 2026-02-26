# open file and store file object in a variable
# file =  open('Module9/Lesson49/FileHandlingPart1/Codingal.txt')
# file=open('fileOutside.txt')
file=open('FileHandling/FileHandlingp1/file1.txt')

# read the contents of file
print(file.read()) # Python will just load the contents of the file and give it to you as a string

# close the file
file.close()