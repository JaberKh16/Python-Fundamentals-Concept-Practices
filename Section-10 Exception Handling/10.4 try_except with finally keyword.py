"""
    Try Except Block With Finally
    ============================
    Syntax-
        try:
            statement
        except Exception:
            statement
        finally:
            statement
    
    Note:   Whether program exectuion hits the exception or not finally
            block will run always.

"""

try :
    print(11/0) # mathematical error division by zero
except ZeroDivisionError:
    print("Divided by Zero.")
finally:
    print("Code Portion after the exception hits.")