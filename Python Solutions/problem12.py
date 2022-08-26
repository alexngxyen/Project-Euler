#  ============================================================================
#  Name        : problem12.py
#  Description : Finds the value of the first triangle number to have over five 
#                hundred divisors.
#  Author      : Alex Nguyen
#  Date        : August 2022
#  ============================================================================

# Import Packages
import timeit

# Function
def numberOfDivisors(n):
    # Initialize Variables
    divisor_length = 0
    
    # Loop through all numbers from 1 to n
    for i in range(1, n+1):
        # Check if n is divisible by i
        if n % i == 0:
            # Increment Divisors
            divisor_length += 1
            
    # Return Divisors
    return divisor_length

# Start Timer
start = timeit.default_timer()

# Initialize Parameters
number_of_divisors             = 500
triangle_number_divisor_length = 0
triangle_number                = 1
count                          = 1

# Compute the Number of Divisors for the Triangle Number
while triangle_number_divisor_length < number_of_divisors:
    # Factor Triangle Number
    triangle_number_divisor_length = numberOfDivisors(triangle_number)
    
    # Check Triangle Number's Divisors
    if triangle_number_divisor_length < number_of_divisors:
        # Increment Count
        count += 1

        # Increment Triangle Number
        triangle_number += count
            
# End Timer
end = timeit.default_timer()

# Print Results
print("\nValue of the triangle number with over", number_of_divisors, "divsors =", triangle_number)
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds\n")            