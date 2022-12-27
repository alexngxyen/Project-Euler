#  ============================================================================
#  Name        : problem_20.py
#  Description : Find the sum of the digits in the number 100! (100 factorial)
#  Author      : Alex Nguyen
#  Date        : August 2022
#  ============================================================================

# Import Packages
import timeit
import math

# Start Timer
start = timeit.default_timer()

# Initialize Parameters
n = 100
factorial_value = math.factorial(n)
sum_of_digits  = 0

# Compute Factorial Digit Sum
string_factorial_value = str(factorial_value) 

for i in range(len(string_factorial_value)):
    # Sum Digits
    sum_of_digits = sum_of_digits + int(string_factorial_value[i])

# End Timer
end = timeit.default_timer()

# Print Results
print("\nSum of the digits of the number {}!".format(n), "=", sum_of_digits)
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds\n")      