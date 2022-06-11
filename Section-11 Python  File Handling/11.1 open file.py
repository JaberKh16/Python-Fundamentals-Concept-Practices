"""
    Working With Files using open() Function
    =========================================
    In Python, a built-in function open() is used to work with
    the files. It returns an File Obejct.
    Syntax-
        open("file.ext", "access_mode")
    
    For Example-
        To work with file we need first open a file with open() function
            e.g-    file1 = open("filename.txt", "r") 
    
    Some of the Access Mode
    ------------------------
    a) 'r'  --> to open a file as read-only mode and starts reading
                from the begining of the file.
    b) 'a'  --> to open a file as appending mode and pointer is placed
                at the end of file and if file is not existed then creates a
                new file with the specified name.
    c) 'w'  --> to open a file as write-only mode and pointer is place at
                the begining thus overwrites the content of the file while perform
                writing and if the specified file is not existed then creates
                a new file with the specified name.
    d) 'rb' --> to open a file as read-only mode in binary format and starts
                reading from the beginning of the file. While binary format can be 
                used for different purposes such as when dealing with things 
                like- images, videos, etc.
    d) 'wb  --> to open a file as writing mode in binary format.
    e) 'wb+'--> to open a file as reading and writing mode in binary format.
    f) 'r+' --> to open a file as a reading and writing mode and place the pointer
                at the begining of the file.
                
    g) 'w+' --> to open a file as reading and writing mode.
    h) 'a+' --> to open a file as reading and writing mode.
    i) 'ab' --> to open a file as appending mode in binary format.
    j) 'ab+'--> to open a file as appending and reading mode in binary format.
    
    
    When working with the files its better to enclose the open() operation
    inside a try except block so that whenever any issue occurs opening or
    accessing files it can be handled easily. 
    
    Note: Must remember to close the file after the operations being done, 
        otherwise many issues might occurs later including this holds particular
        memory which is an one issue.

"""

# it returns a FileNotFoundError exception
# to handle the exception we can use try/except block
# it helps programme terminate with even if having exceptions

# try :
#     file1 = open("filename.txt","r") # opening the file as reading mode 
#     file1.close()
# except FileNotFoundError:
#     print("File isn't available in this directory address.")

file1 = open("filename.txt","r") # opening the file as reading mode 
file1.close()