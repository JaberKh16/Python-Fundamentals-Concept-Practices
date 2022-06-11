"""
    Exception Handling In Python
    ============================
    Exception is an event which is nothing but the errors which happends
    due to certain logic misinterpreting, misspelled of syntax etc. 
    occurs during the execution of a program that disrupts the normal 
    flow of the program's instructions. 
    
    In general, when a Python script encounters a situation that it cannot 
    cope with, it raises an exception. 
    
    An exception is a Python object that represents an error.
    
    Some Of The Exception In Python
    -------------------------------
    AssertionError		    #   Raised when assert statement fails.
    AttributeError			#   Raised when attribute assignment or reference fails.
    EOFError				#   Raised when the input() functions hits end-of-file condition.
    FloatingPointError		#   Raised when a floating point operation fails.
    GeneratorExit			#   Raise when a generator's close() method is called.
    ImportError				#   Raised when the imported module is not found.
    IndexError				#   Raised when index of a sequence is out of range.
    KeyError				#   Raised when a key is not found in a dictionary.
    KeyboardInterrupt		#   Raised when the user hits interrupt key (Ctrl+c or delete).
    MemoryError				#   Raised when an operation runs out of memory.
    NameError				#   Raised when a variable is not found in local or global scope.
    NotImplementedError		#   Raised by abstract methods.
    OSError					#   Raised when system operation causes system related error.
    OverflowError			#   Raised when result of an arithmetic operation is too large to be represented.
    ReferenceError			#   Raised when a weak reference proxy is used to access a garbage collected referent.
    RuntimeError			#   Raised when an error does not fall under any other category.
    StopIteration			#   Raised by next() function to indicate that there is no further item to be returned by iterator.
    SyntaxError				#   Raised by parser when syntax error is encountered.
    IndentationError		#   Raised when there is incorrect indentation.
    TabError				#   Raised when indentation consists of inconsistent tabs and spaces.
    SystemError				#   Raised when interpreter detects internal error.
    SystemExit				#   Raised by sys.exit() function.
    TypeError				#   Raised when a function or operation is applied to an object of incorrect type.
    UnboundLocalError		#   Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable.
    UnicodeError			#   Raised when a Unicode-related encoding or decoding error occurs.
    UnicodeEncodeError		#   Raised when a Unicode-related error occurs during encoding.
    UnicodeDecodeError		#   Raised when a Unicode-related error occurs during decoding.
    UnicodeTranslateError	#   Raised when a Unicode-related error occurs during translating.
    ValueError				#   Raised when a function gets argument of correct type but improper value.
    ZeroDivisionError		#   Raised when second operand of division or modulo operation is zero.1) Attribute Error
    
    To handline Python Exception try except block is used which have the following
    syntax-
        try:
            statement
        except Exception_Name:
            statement

"""
try :
    num1 = 7
    num2 = 0
    print(num1 / num2) # hits the exception because evalautes to 7/0
    print("Done of Calculation.")
    
except ZeroDivisionError:
    print("Divided by Zero.")
    print("Occurred due to zero division.")