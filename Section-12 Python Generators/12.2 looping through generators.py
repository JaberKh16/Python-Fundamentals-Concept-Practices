'''
    Generator Concept In Python
    ===========================
    # Generator are nothing but the iterators
    # It can only iterate over once in a lifetime, thus it doesn't store
      all value in memory.
    # Can generates the values on the fly to get the values just need to
      loop over it or can pass it with a help of functions.
    # But most of the time, Generators are implemented as functions
      and it doesn't return any value, but yield it.
    # where, 'yield' is keyword in Python is like the 'return' statement
      in a function, when done so the function instead of returning the
      output it returns the generator that can be iterated upon.
      
      Each time you iterate, Python runs the code until it encounters a
      'yield' statement inside the function. Then, it sends the 
      yielded value and pauses the function in that state 
      without exiting.
      
      When the function is invoked the next time, the state at which 
      it was last paused is remembered and execution is continued 
      from that point onwards. This continues until the generator 
      is exhausted.
      
      Since the 'yield' enables the function to remember its ‘state’, 
      this function can be used to generate values in a logic defined 
      by you. So, it function becomes a "Generator".
      
      
      Note: Calling the Generator the second time wont give anything. 
            Because the Generator Object is already exhausted and 
            has to be re-initialized.

'''


# defining the generator function
def generator_function() :
    for i in range (1,10) :
        yield i*i

# assign the generator funciton into some variable
generator_object = generator_function()


# getting values via looping over the generator function
for generates_values in generator_object:
    print(generates_values)
