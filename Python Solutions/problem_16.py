#  ============================================================================
#  Name        : problem_16.py
#  Description : Find a starting number under one million which produces the 
#                longest Collatz sequence.
#  Author      : Alex Nguyen
#  Date        : August 2022
#  ============================================================================

# Import Packages
import timeit

# Start Timer
start = timeit.default_timer()

# Initialize Parameters
exponent_value = 1000
power_digit    = 2**exponent_value
sum_of_digits  = 0

# Compute Power Digit Sum
string_power_digit = str(power_digit) 

for i in range(len(string_power_digit)):
    # Sum Digits
    sum_of_digits = sum_of_digits + int(string_power_digit[i])

# End Timer
end = timeit.default_timer()

# Print Results
print("\nSum of the digits of the number 2**{}".format(exponent_value), "=", sum_of_digits)
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds\n")      