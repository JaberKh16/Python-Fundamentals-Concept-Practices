"""
    Appending The File Content Using Append Access Modifier
    -------------------------------------------------------
    Need to open the file as a appending mode through specifying the
    append access modifier. For Example-
        
            open('filename.ext', 'a') # opening the file appending 'a' mode
            
    Note: While appending content to the appending start from the last pointer
        the file already have been written.
"""

try :
    
    # opening the file in windows
    # file1 = open("C:\\Users\Jaber\PycharmProjects\Python Practice Programm\Section -11 File handling\example3", "a")
    
    # opening the file in linux
    file1 = open('./Files/example-3.txt', 'a') # opening as appending mode
    
    first_text = "This is awesome working with files"
    # adds content to the existing file
    content_added = file1.write(first_text)
    print(content_added)
    
    # adds content to the existing file
    second_text =("I dont know")
    content_added = file1.write(second_text)
    print(content_added)
    
    # closing the file
    file1.close()
    
except FileNotFoundError:
    print("File is not available")