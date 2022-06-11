"""
    File Accessing Mode Supported In Python
    ========================================
    
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
    
    
"""

try :
    file1 = open("./Files/example-8.txt", "r+") # 'r+' mode
    content = file1.read()
    print(content)
    file1.close()

    file1 = open("./Files/example-8.txt", "w") # 'w' mode

    write_content = "i am awesome."
    content1 = file1.write(write_content)
    print(content1)
    file1.close()

    # writing on the file
    file1 = open("./Files/example-8.txt", "a") # 'a' mode
    append_content = "\nPython is fun"
    content1 = file1.write(append_content)
    print(content1)
    file1.close()

    file2 = open("./Files/example-8.txt", "r")
    file2.seek(0)
    content =file2.readlines()
    print(content)

    # with r+ mode, can both read and write on the file at a same time
    file1 = open("./Files/example-8.txt", "r+")
    append_content = "\nPython is fun"
    content1 = file1.write(append_content)
    print(content1)
    file1.close()

except FileNotFoundError:
    print(" File is not available here.")

