"""
    Generator yield Defining With try/finally Block
    ===============================================
    'yield' Keyword isn't permitted in the try/finally block 'try'
    part area. Thus, Generator should allocate resources with caution.
    
    However, 'yield' can appear in finally clauses, except clauses, 
    or in the try part of try/except clauses, but not in the try/finally
    clauses.
    
"""

def numberGenerator(n):
    try:
        number = 0
        while number < n:
            yield number
            number += 1
    finally:
        yield n # as a result of the finally clause, the number 10 is 
                # included in the output, and the result is a list of 
                # numbers from 0 to 10. This normally wouldn't happen 
                # since the conditional statement is number < n.

print(list(numberGenerator(10)))