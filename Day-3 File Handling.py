# # Read a txt file
file = open("Day-3 File Handling.txt", "r")
data = file.read()
print("Data of the file is:", data)

# # Write code to open a file named mydata.txt in read mode.
file = open("Day-3 File Handling.txt", "r")
data = file.read()
print("Data of the file is:", data)

# # Write a program to read a text from a given file certificate.txt and find whether it contains word live.
file = open("Day-3 File Handling.txt", "r")
dataoffile = file.read()
dataoffile = dataoffile.lower()
if "live" in dataoffile:
    print("Yes Live word is present in the file")
else:
    print("Not present")

# # Open a file called report.txt in write mode.
file = open("Day-3 File Handling.txt", "a")
file.write("All Set.")
file.write("\nI am a playboy")

# # Read entire file
file = open("Day-3 File Handling.txt", "r")
data = file.read()
file.close()

# with keyword 
with open("Day-3 File Handling.txt", "r") as f:
    data = f.read()
    print("File Data", data)

# read line by line
with open("Day-3 File Handling.txt", "r") as f:
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()
    data = f.read()
    print("Line 1", line1)
    print("Line 2", line2)
    print("Line 3", line3)
    print("File Data", data)

# # read lines
with open("Day-3 File Handling.txt", "r") as f:
    readLinesMethod = f.readlines()
    print(readLinesMethod)

# # Read only the first line of bio.txt
with open("Day-3 File Handling.txt", "r") as f:
    line1 = f.readlines()
    print("Line 1:", line1)

# # Print how many lines are present in notes.txt
import os
with open("Day-3 File Handling.txt", "r") as f:
    listoflines = f.readlines()
    print("Output of readLines Functions:")
    print("Number of Lines in File:", len(listoflines))

# Rename a file
os.rename("Day-3 File Handling.txt", "fuddi.txt")
os.remove("Day-3 File Handling.txt")
