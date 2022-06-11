"""
    Connecting Generators Concept
    =============================
    Since Python 3.3, a new feature allows generators to connect themselves 
    and delegate to a sub-generator.
    
    The new expression is defined in PEP 380 and the Syntax is-

            yield from <expression>
            
    where <expression> is an expression evaluating to an iterable, 
    which defines the delegating generator.
    
    An important application of generators: the capacity to divide a 
    long task into several separate parts, which can be useful 
    when working with big sets of data and chaining of generators
    together are very useful on more of a dynamic programming.
    
"""

def generator_1(n):
    for i in range(n):
        yield i

def generator_2(n, m):
    for i in range(n, m):
        yield i

def generator_3(n, m):
    yield from generator_1(n)
    yield from generator_2(n, m)
    yield from generator_2(n, m+3)

print(list(generator_1(5)))
print(list(generator_2(5, 10)))
print(list(generator_3(0, 10)))