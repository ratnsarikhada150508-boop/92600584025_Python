import os
import sys

os.mkdir("MyFolder")
print("Directory created")


print("Current directory:", os.getcwd())

# Create a file
with open("MyFolder/sample.txt", "w") as f:
    f.write("Hello Python")

print("File created")

# List files and directories
print("Directory contents:", os.listdir("MyFolder"))

# Rename a file
os.rename("MyFolder/sample.txt", "MyFolder/new.txt")
print("File renamed")

# Display Python version
print("Python version:", sys.version)

# Delete file and directory
os.remove("MyFolder/new.txt")
os.rmdir("MyFolder")
print("File and directory deleted")
