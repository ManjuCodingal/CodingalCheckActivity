# open the file in read mode
# open('Module9/Lesson49/FileHandlingPart1/Codingal.txt')
# file_read = open('Module9/Lesson49/FileHandlingPart1/Codingal.txt','r')
# print("File in Read Mode -")
# print(file_read.read())
# file_read.close()

# open the file in write mode
file_write = open('FileHandling/FileHandlingp1/file2.txt', 'w')
# write in the file 
file_write.write(" File in write mode ....")
file_write.write("Hi! I am Penguin. I am 1 yr. old. I like dancing ")
file_write.close()

# open the file in append mode
# file_append = open('Module9/Lesson49/FileHandlingPart1/Codingal.txt', 'a')
# # append in the file 
# file_append.write("\n File in append mode ....")
# file_append.write("Hi! I am Penguin. I am 1 yr. old")
# file_append.close()