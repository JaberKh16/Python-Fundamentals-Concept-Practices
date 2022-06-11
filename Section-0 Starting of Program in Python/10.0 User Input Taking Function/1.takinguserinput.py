'''
        Python Input Stream----> input(prompt)
                Syntax : input(prompt)

        ## via input(prompt) can prompt the console to take user input and then
        ## prints the value given in input() stream, until user press 'Enter'
        ## here, keyboard stroke "Enter" is breaking condition for the input() stream.
        
                input("Write Something")
                input(2)
                input(32.5)
                input("a")
        
        Normally, the input() function takes user input as a string object. So, if we
        want to work with other datatype needs to be explitly cast the input() stream 
        to another datatype.
'''

# via prompting the console
input("Write Something\n")
input(2)

# via variable declaring
x =input("Hi\n")
print(x) #returns the string and take then take input

# with int() function
x = int(2)
print(x)  #return int
print(type(x))

## casting the input() with others datatype object,say for example--> data_type(input()) function

# takes the input and convert it to integer object
# thus integer value needs to be provided otherwise will get "ValueError" exception
x =int(input("Takes only the Integer input:\n"))   # enter Integer type

# takes the input and convert it to float type , so either integer or float type data
# can be provided as input, otherwise will get an "ValueError" exception
x =float(input("Takes only the float input:\n"))   # enter either integer or float type

# chr(int) to perform a character operation over the user input, this 
# chr(int) value as input an convert it to a ASCII Character.
x =chr(input("Takes only the character input:\n")) # enter a character

# takes a single character or a string as input and converted it to string object 
x =str(input("Takes only the string input:\n"))   # enter a character or a string

x = int('') # int cant take string type
print(x)   # gives u a ValueError : Invalid literal for int()







