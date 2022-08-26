#  ============================================================================
#  Name        : problem3.py
#  Description : Finds the largest prime factor of the number 600851475143.  
#  Author      : Alex Nguyen
#  Date        : August 2022
#  ============================================================================

# Import Packages
import timeit

# Start Timer
start = timeit.default_timer()

# Function to Determine Prime Factors
def determinePrimeFactors(number):
    """ This function determines the prime factors of a given number. """
    # Initialize Parameters
    prime_factors = []
    count         = 1
    divisor       = 2
    
    while count < number:
        if number % divisor == 0:
            prime_factors.append(divisor)
            number = number / divisor
            count  = 1
        else:
            count   += 1
            divisor += 1
    
    return prime_factors

# Initialize Parameters
value = 600851475143                              # Value of Interest

# End Timer
end = timeit.default_timer()

# Print Results
print("\nLargest prime factor of the number", value,  "=", max(determinePrimeFactors(value)))
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds\n")
