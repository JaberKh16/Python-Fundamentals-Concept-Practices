'''
    Format e.g --->    if expression :
                                statement1
                                statement2

                        else expression:
                                if expression :
                                else :
                        else :



'''

x =int(input("Enter the number :\n"))
if x >0 :
    print("It's a positive number")

    if (x % 2==0) :
        print("number is even number :", x)
    else  :
        if(x %2 !=0) :
            print("It's odd number :", x)
        else :
            print("We r going check for another condition")


else :
    print("Invalid")

print("We r done !!! \n")
