#create a new file
# new_file = open('New_File.txt', 'x')
# new_file.close()

#check if a file exists 
import os
print("Checking if my_file exists or not....")
if os.path.exists("my_file.txt"):
  os.remove("my_file.txt")
else:
  print("The file does not exist")

#create a new if it doesn't
my_file = open("my_file.txt", "w")
my_file.write("Hi! I am Penguin and I am 1 yr old.")
my_file.close()

#delete file named codingal
os.remove('my_file.txt')

#delete the folder
# os.rmdir('Folder')  #folder should be empty

# if os.path.exists('Folder'):
#     if not os.listdir('Folder'):  # Check if it's empty
#         os.rmdir('Folder')
#         print("Folder deleted.")
#     else:
#         print("Folder is not empty.")
# else:
#     print("Folder does not exist.")

# MyTxtFile.txt : Hi! I am Penguin and I am 1 yr old.
# NewFile.txt as empty