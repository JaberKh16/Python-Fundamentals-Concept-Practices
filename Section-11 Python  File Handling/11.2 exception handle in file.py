""" 
    Exception Handling While Working With File
"""

# Opening a file within the try except block 
try :
    file1 = open("filename.txt", "r")
    file1.close() # close() method to close the file
except FileNotFoundError :
    print("File is not found or available.")
