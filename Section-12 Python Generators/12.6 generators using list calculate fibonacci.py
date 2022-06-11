"""
    Example Of Generator Yielding List
"""
def fibonacci_series(number) :
    a = b= 1
    result = []
    for i in range(number) :
        result.append(a) # appending to the list
        a, b =b, a + b
    yield result


for series_values in fibonacci_series(5):
    print(series_values)