#  ============================================================================
#  Name        : problem_26.py
#  Description : Find the value of d < 1000 for which 1/d contains the longest
#                recurring cycle in its decimal fraction part.
#  Author      : Alex Nguyen
#  Date        : December 2022
#  ============================================================================

# Import Packages
import timeit

# Functions
def length_of_recurring_cycle(numerator, denominator):
    # Initialization
    length = 0
    digits = []
    remainder = numerator % denominator
    
    # No Recurring Cycle
    if remainder == 0:
        return length, digits
    
    # Recurring Cycle
    remainder_list = [remainder]
    while True:
        remainder *= 10
        digits.append(remainder // denominator)
        remainder = remainder % denominator
        
        if remainder == 0:
            return length, digits
        
        if remainder in remainder_list:
            length = len(remainder_list) - remainder_list.index(remainder)
            return length, digits[remainder_list.index(remainder):]
        remainder_list.append(remainder)

# Start Timer
start = timeit.default_timer()

# Initialize Parameters
threshold                 = 10**3
largest_cycle_denominator = 0
largest_cycle_length      = 0
largest_cycle_digits      = []

# Compute Longest Recurring Cycle
for k in range(1, threshold + 1):
    # Compute Length of Recurring Cycle\
    length, digits = length_of_recurring_cycle(1, k)
    
    # Update Largest Recurring Cycle
    if length > largest_cycle_length:
        largest_cycle_length       = length
        largest_cycle_digits       = digits
        largest_cycle_denominator  = k
      
# End Timer
end = timeit.default_timer()

# Print Results
print("\nDenominator with the longest recurring cycle in its decimal fraction part = {}".format(largest_cycle_denominator))
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds\n")      