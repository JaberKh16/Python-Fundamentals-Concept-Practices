"""
    read(), readlines() and seek() Functions Concept
    ================================================
    1.  read() Function is used read the content from a specified file.
    
        It is a method of File Object which is used to read the whole content
        of a specified file and gets it pointer at the last. It reads the 
        content as a byte by byte context. 
    
    2.  readlines() Function is also used to the read the file content as 
        line by line context and returns a list of each line content. After
        the content has been read it returns the pointer at the end of 
        last read line.
        
    3.  seek() Function is used to set the pointer of read content at
        any point of index and returns a list containing item of 
        split at keywords escaped sequence.
"""

try :
    file1 = open("./Files/example-1.txt", "r")
    # read() with no argument read whole of the text file
    ## gets point at all bytes been read
    print(file1)
    content = file1.read()
    print(content)

    # #it returns [] list after reading the file and points at last
    # ## after reading the line points end the of example file data
    # ## now because of file content is already read so it return a
    # ## a empty list e.g []
    # content1 = file1.readlines()
    # print(content1)


    # ## to get back the pointer at start and read the from start
    # ## we need to use seek() function
    # ## seek() function returns a list containing item of split at keywords
    # ## escape sequence
    file1.seek(0)
    content2 = file1.readlines()
    print(content2)

    # getting the content using list comprehension technique
    content = [i.rstrip("\n") for i in content]
    print(content)
    content = [i.rsplit("\n") for i in content]
    print(content)
    # #it returns a <generator object <genexpr> at 0x01b510b0>
    # # means via generator object returns file physical address
    # content = (i.r("\n") for i in content)
    # print(content)

    # to close the file
    file1.close()

except FileNotFoundError:
    print("File is not available")



