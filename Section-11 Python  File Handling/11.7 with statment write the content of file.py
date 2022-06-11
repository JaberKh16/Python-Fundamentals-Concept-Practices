"""
    Working With Files using with Statement
    ========================================
    In Python, a built-in function open() is used to work with
    the files. It returns an File Obejct, where 'with' keyword
    is used along with it open() to provide an alias to the 
    File Object.
    Syntax-
        with open("file.ext", "access_mode") as file:
            statement
    
    Some of the Access Mode
    ------------------------
    a) 'r'  --> to open the file as a reading mode
    b) 'a'  --> to open the file as a appending mode
    c) 'w'  --> to open the file as a writing mode
    d) 'rb'  --> to open the file as a reading in binary mode
    d) 'wb'  --> to open the file as a writing in binary mode
    
    
    When working with the files its better to enclose the file operations
    inside a try except block so that whenever any issue occurs opening or
    accessing files it can be handled easily. 
    
    Note: Must remember to close the file after the operations being done, 
        otherwise many issues might occurs later including this holds particular
        memory which is an one issue.
    
        
"""

try :
    with open("./Files/example-5.txt", "w") as file:
        first_content = "I m adding new data to the file content"
        content = file.write(first_content)
        
        # Note: Each word is a single byte.
        print('first_content: {} bytes'.format(content)) # returns the byte size been written
        
        second_content = "\nWanna add something more in file"
        updated_content = file.write(second_content)
        
        # Note: Each word is a single byte.
        print('second_content: {} bytes'.format(updated_content)) # returns the byte size been written
        
        # closing the file
        file.close()

except FileNotFoundError:
    print("File is not available.")

finally:
    print("\nWriting has been done.")