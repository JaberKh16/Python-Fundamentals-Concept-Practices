"""
    Try Exception Block Accepting All Kind Of Exceptions 
"""

try :
    num = 10/0
except: # using only the 'except' keyword means accepting all kinds of Python Exceptions
    print("Divided by Zero.")
finally:
    print("Execution done.")
