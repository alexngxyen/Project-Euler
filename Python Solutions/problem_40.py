#  ============================================================================
#  Name        : problem_40.py
#  Description : Find the value of the product of several digits from an irrational 
#                decimal fraction.
#  Author      : Alex Nguyen
#  Date        : December 2022
#  ============================================================================

# Import Packages
import timeit

# Start Timer
start = timeit.default_timer()

# Initialize Parameters
max_number     = 10**6
decimal_string = "" 
digit_product  = 1
digit_list     = [1, 10, 100, 1000, 10000, 100000, 1000000]

# Create Irrational Decimal Fraction by Concatenating Positive Integers
for k in range(1, max_number + 1):
    decimal_string += str(k)

# Compute Product of Digits
for digit in digit_list:
    digit_product *= int(decimal_string[digit - 1])

# End Timer
end = timeit.default_timer()

# Print Results
print("\nProduct of several digits from the irrational decimal fraction = {}".format(digit_product))
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds\n")      