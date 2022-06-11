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


'''

x =int(input("Enter the number :\n"))
if x <0 :
    print("It's a negative number")

    if (x % 2 ==0):
        print("greater than 10", x)
    if(x % 2 != 0):
        print("It's odd number", x)
    if(x==str(x)) :
        print("It's now an string", x)


print("We r done !!! \n")
