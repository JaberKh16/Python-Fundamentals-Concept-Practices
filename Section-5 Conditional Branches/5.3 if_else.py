'''
    Format e.g --->    if expression :
                                statement1
                                statement2
                                statement3
                                if expression :
                                        statement1
                                        statement2
                                if expression :
                                        statement1
                        else :
                            statement1


'''

x =int(input("Enter the number :\n"))
if x >0 :
    print("It's a positive number")

    if (x % 2 ==0):
        print("number is even :", x)
    if(x % 2 != 0):
        print("It's odd number", x)
    if(x==str(x)) :
        print("It's now an string", x)
else :
    print("Invalid")

print("We r done !!! \n")
