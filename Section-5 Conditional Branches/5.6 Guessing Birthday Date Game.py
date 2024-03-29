"""
    Guessing Birthday Game
    -----------------------
    This program provides the birthday date depending on the boolean
    base checking provided throgh the user. Where basically the boolean
    check is used for adding some particular values depending on the
    provided value of 0 or 1 which selects some appending values for date
    variable from the date set which then evaluates to the actual date value. 
    
    eval() method parses the expression passed to this method 
    and runs python expression (code) within the program.
    
    eval(expression, gloabals=None, locals=None) where those
    parameter literally defines the following-
    1) expression -- the string parsed and evaluated as a Python expression 
    2) globals (optional) - a dictionary
    3) locals (optional)- a mapping object. Dictionary is the standard 
                        dictionary and commonly used mapping type in Python


"""
day = 0 # birth day to be determined

# Prompt the user to answer the first question
question1 = "Is your birthday in Set1\n" + \
            " 1 3 5 7\n" + \
            " 9 11 13 15\n" + \
            "17 19 21 23\n" + \
            "25 27 29 31" + \
            "\nEnter 0 for No and 1 for Yes: "
answer = eval(input(question1)) # used to evaluate the expression of 'question1'

if answer == 1:
    day += 1 # appending 1 to it

# Prompt the user to answer the second question
question2 = "Is your birthday in  Set2?\n" + \
            " 2 3 6 7\n" + \
            "10 11 14 15\n" + \
            "18 19 22 23\n" + \
            "26 27 30 31" + \
            "\nEnter 0 for No and 1 for Yes: "
answer = eval(input(question2)) # used to evaluate the expression of 'question2'

if answer == 1:
    day += 2

# Prompt the user to answer the third question
question3 = "Is your birthday in Set3?\n" + \
            " 4 5 6 7\n" + \
            "12 13 14 15\n" + \
            "20 21 22 23\n" + \
            "28 29 30 31" + \
            "\nEnter 0 for No and 1 for Yes: "
answer = eval(input(question3)) # used to evaluate the expression of 'question3'

if answer == 1:
    day += 4

# Prompt the user to answer the fourth question
question4 = "Is your birthday in Set4?\n" + \
            " 8 9 10 11\n" + \
            "12 13 14 15\n" + \
            "24 25 26 27\n" + \
            "28 29 30 31" + \
            "\nEnter 0 for No and 1 for Yes: "
answer = eval(input(question4)) # used to evaluate the expression of'question4'

if answer == 1:
    day += 8

# Prompt the user to answer the fifth question
question5 = "Is your birthday in Set5?\n" + \
            "16 17 18 19\n" + \
            "20 21 22 23\n" + \
            "24 25 26 27\n" + \
            "28 29 30 31" + \
            "\nEnter 0 for No and 1 for Yes: "
answer = eval(input(question5))  # used to evaluate the expression of 'question5'

if answer == 1:
    day += 16

print("\nYour birthday is on " + str(day) + "day!")
