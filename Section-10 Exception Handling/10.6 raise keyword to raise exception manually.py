"""
    Raising Exception In Python
    ===========================
    To raise an exception inside the Python code, for certain
    condition can use the keyword 'raise' to throw or raise an
    exception by yourself. This 'raise' keyword is used to
    manually raise an exception.
    
    Very useful in some cases when programmer wants to show some
    warning saying that those features cant be usable.
    
    Syntax-
        Can be raise exception in two ways-
            1) using parenthesis () 
                e.g-  raise ExceptionName("")
                
            2) using just the keyword
                e.g- raise Exception

"""

# it raising the 'ZeroDivisionError' Exception
try :
    number = 7/0
except:
    print("Divided by Zero.")
    raise

# raising the 'ValueError' Exception
print(1) # trying print some code before raising exception

raise ValueError # 'raise' is used to raise the specified Exception

print(2)

# if want to raise the 'NameError' Exception then uncomment the code
name = "133"
raise NameError("Invalid Name!")


