'''
    Format e.g --->    if expression :
                                statement1
                                statement2
                                statement3
                        elif expression :
                                if expression :

                                elif expression:

                        else :


'''

x =int(input("Enter the number :\n"))
if x ==5 :
    print("It's a positive number and it's 5")

elif (x > 20) :
        print("number is greater than 20 and it is :", x)

        if(x %2 ==0) :
            print("It's a even number :", x)
        elif (x %2!=0):
            print("It's an odd number :", x)



else :
    print("Invalid")

print("We r done !!! \n")
