'''
    # Blueprint : lambda (args) : manipulate(args)
    # Python has lambda keyword to work in a one expression or one line
    # lambda is basically a inline function i.e one line function
    # it is also a anonymous function i.e nameless function
    # About args --> lambda can take many arguments as you specified
    # manipulate can be a lambda function which is basically call a nested
      lambda function (function within a function)
      e.g
            x = lambda c : lambda a, b : lambda d: (c * (a + b)) %d
'''

# works with lambda keyword


# works with single arguments
x = lambda x : x**2 + 5*x + 4
# it returns the function along with it's address
# e.g   <function <lambda> at 0x00B117C8>
print(x)

# to display the expression value need to call it through parameter
# print(x (2))
# we will learn it in the next part


# lambda can take many arguments

# it returns the function type along with address
# e.g <function <lambda> at 0x02B693D8>
x = lambda x , y, z: x**2 + 4*y -z
print(x)


# returns the type with physical address
# e. g  <function <lambda> at 0x03349390>

x = lambda  x : lambda a, b : lambda c, d, e : lambda f : ((a* b +x) % x + (c -d + e )) *f
print(x)
