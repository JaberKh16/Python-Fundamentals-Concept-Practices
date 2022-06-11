
# Example-1
def sum(number) :
    if number ==0:
        return 
    else :
        return number + sum(number-1)
print(sum(10))
print(sum(0))

# Example-2
def trail_sum(x, accumulator = 0) :
    if x == 0 :
        return accumulator
    else :
        return trail_sum(x-1, accumulator + x)
print(sum(10))
print(trail_sum(0))

