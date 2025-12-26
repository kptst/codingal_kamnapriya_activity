# write in file using with()function
with open('Codingal.txt', 'w') as file:
  file.write("Hi! I am Penguin and I am 1 yr old.")
file.close()

# split file into words
with open('Codingal.txt', 'r') as file:
  data = file.readlines()
  print("Words in this file are....")
  for line in data:
    word = line.split()
    print (word)
file.close()


#ACTIVITY-2

#create a new file
new_file = open('New_File.txt', 'x')
new_file.close()

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
os.remove('Codingal.txt')

#delete the folder
os.rmdir('Folder')




#ACTIVITY-3

# Program to eliminate repeated lines from a file

# creating the output file
outputFile = open('UpdatedFile.txt', "w")

# reading the input file
inputFile = open('Repeated.txt', "r")

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


#ACTIVITY-4
# Program to merge two files into a third file


# Reading data from file1
with open('Codingal.txt') as fp:
	data1 = fp.read()

# Reading data from file2
with open('sample_doc.txt') as fp:
	data2 = fp.read()
	
# Merging 2 files
# To add the data of file2
# from next line
data1 += "\n"
data1 += data2
print("Merging two files....")
with open ('MergedFile.txt', 'w') as fp:
	fp.write(data1)


# # =========================
# # ACTIVITY - 1
# # =========================

# # Write in file using with() function
# with open('Codingal.txt', 'w') as file:
#     file.write("Hi! I am Penguin and I am 1 yr old.")

# # Split file into words
# with open('Codingal.txt', 'r') as file:
#     data = file.readlines()
#     print("Words in this file are....")
#     for line in data:
#         words = line.split()
#         print(words)


# # =========================
# # ACTIVITY - 2
# # =========================

# import os

# # Create a new file
# open('New_File.txt', 'w').close()

# # Check if file exists
# print("\nChecking if my_file exists or not....")
# if os.path.exists("my_file.txt"):
#     os.remove("my_file.txt")
# else:
#     print("The file does not exist")

# # Create file if it does not exist
# with open("my_file.txt", "w") as my_file:
#     my_file.write("Hi! I am Penguin and I am 1 yr old.")

# # Delete Codingal.txt
# if os.path.exists('Codingal.txt'):
#     os.remove('Codingal.txt')

# # Create and delete a folder
# os.makedirs('Folder', exist_ok=True)
# os.rmdir('Folder')


# # =========================
# # ACTIVITY - 3
# # =========================

# # Program to eliminate repeated lines from a file

# # Create input file
# with open('Repeated.txt', 'w') as f:
#     f.write("Hello\nHi\nHello\nWelcome\nHi\n")

# # Create output file
# outputFile = open('UpdatedFile.txt', "w")
# inputFile = open('Repeated.txt', "r")

# lines_seen_so_far = set()
# print("\nEliminating duplicate lines....")

# for line in inputFile:
#     if line not in lines_seen_so_far:
#         outputFile.write(line)
#         lines_seen_so_far.add(line)

# inputFile.close()
# outputFile.close()


# # =========================
# # ACTIVITY - 4
# # =========================

# # Program to merge two files into a third file

# # Recreate Codingal.txt
# with open('Codingal.txt', 'w') as f:
#     f.write("This is Codingal file.")

# # Create second file
# with open('sample_doc.txt', 'w') as f:
#     f.write("This is sample document file.")

# # Read both files
# with open('Codingal.txt') as fp:
#     data1 = fp.read()

# with open('sample_doc.txt') as fp:
#     data2 = fp.read()

# # Merge files
# data1 += "\n" + data2
# print("\nMerging two files....")

# with open('MergedFile.txt', 'w') as fp:
#     fp.write(data1)


# # =========================
# # SHOW FILES IN COLAB
# # =========================
# print("\nFiles created in Colab:")
# !ls
