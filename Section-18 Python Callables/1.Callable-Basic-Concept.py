'''
    Python Callables Basic Concept
    ==============================
    Callables are those which can be called like functions- it is
    basically a object that can be called upon.
    
    In Python, Functions and Objects are callables. For example-
    when we define a function like-
    >>> def function_name:
            print('Something')
    >>> print(function_name) #  returns <function greet at 0x7f61693c5940>
                                which is a function object
                                
    Now, this function object can be called upon with parenthesis ().
    
    So, every function in Python is a callable, meaning it's an 
    object that you're able to call.

    As said, objects are callable too. For Example-
    >>> colors = ['red', 'green', 'black']
    >>> enumerate(colors) # returns a enumerate object
    >>> print(list(enumerate(colors))) # to see its values

    Now if the enumerate simply being we can see that its basically
    a class.
    >>> print(enumerate) # returns <class 'enumerate'>
    
    In Python we think in terms of "Duck Typing". So if something is a
    function-like object (meaning it acts like a function) we may simply 
    call it "a function".
    The built-in enumerate() function acts like a function (you call it 
    using parenthesis) which means it's basically a function. 
    But more properly, enumerate is a callable, meaning it's 
    an object that can be called.

    Functions can be called and classes can be called. So both functions 
    and classes are callables in Python.

'''

# defining the function
def send_greeting(msg):
    return "Hello " + msg

print(send_greeting); # returns a function object
print(send_greeting("Have Greetings."))


# defining the enumerate callable
colors = ['red', 'green', 'black']
print(enumerate(colors)) # returns a enumerate object
print(list(enumerate(colors))) # returns the result