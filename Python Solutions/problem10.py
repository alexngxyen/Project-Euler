#  ============================================================================
#  Name        : problem10.py
#  Description : Finds the sum of all primes below two million.  
#  Author      : Alex Nguyen
#  Date        : August 2022
#  ============================================================================

# Import Packages
import timeit
import math

# Functions
def isPrime(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

# Start Timer
start = timeit.default_timer()

# Initialize Parameters
value            = int(2e6)                              # Value of Interest
prime_numbers    = []                                    # List of Prime Numbers
count            = 1                                     # Counter

# Determine List of Prime Numbers
while count < value:
    # Check if Prime Number
    if isPrime(count):
        # Add number to list of prime numbers
        prime_numbers.append(count)
    
    # Update Counter
    count += 1

# Sum of Prime Numbers
sum_of_primes = sum(prime_numbers[1:])

# End Timer
end = timeit.default_timer()

# Print Results
print("Sum of all prime numbers below", value, "=", sum_of_primes)
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds")