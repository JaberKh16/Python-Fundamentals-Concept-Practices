"""
    break Statement
    ---------------
    break Statement is used inside the loop to completly break/stop
    the execution of the loop for a certain condition.
    
"""
i = 0
while i<10 :
    print(i)
    i=i+1

    if i>=5 :
        print("Breaking")
        break

print("finished")

