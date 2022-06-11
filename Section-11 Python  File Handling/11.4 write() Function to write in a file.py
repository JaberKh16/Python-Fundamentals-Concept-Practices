"""
    write() Function Concept
    ========================
    write() Function is used to write content inside the file. Generally,
    the content type needs to be in string formatted. This function
    returns the amount of bytes it written using the write() function.
    
    Note : a string type can only pass through a write() as an argument
    else it gives an error called TypeError : write() argument must
    be string , not _other type_name
"""
try :
    # opening the file as writing mode
    file1 = open("./Files/example-2.txt", "w")
    
    first_text ="hello Python"
    second_text = ("\nthis is second line")
    content1 = file1.write(first_text)
    content2 = file1.write(second_text)
    
    # third_text = "\n2, 43, 354,"
    # content3 = file1.write(third_text)
    
    print('Content1 wrotes:{} bytes and Content2 wrotes: {} bytes'.format(content1,content2)) # returns the size of bytes gets been written
    
    # closing the file
    file1.close()
except FileNotFoundError:
    print("File is not available")