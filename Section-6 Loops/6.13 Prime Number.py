"""
    Example Of Prime Numbers From 2 to 1000
"""

NUMBER_OF_PRIMES = 1000 # Number of primes to display
NUMBER_OF_PRIMES_PER_LINE = 10 # Display 10 per line
count = 0 # Count the number of prime numbers
number = 2 # A number to be tested for primeness

print("The first 50 prime numbers are between 2 to 1000-")

# Repeatedly find prime numbers
while count < NUMBER_OF_PRIMES:
    # Assume the number is prime
    isPrime = True # Is the current number is prime?

    # Test is number is prime
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, the number is not prime
            isPrime = False # Set isPrime to false
            break # Exit the for loop
        divisor += 1

    # Display the prime number and increase the count
    if isPrime:
        count += 1 # Increase the count

        print(format(number, "5d"), end = '')
        if count % NUMBER_OF_PRIMES_PER_LINE == 0:
            # Display the number and advance to the new line
            print() # Jump to the new line

    # Check if the next number is prime
    number += 1
