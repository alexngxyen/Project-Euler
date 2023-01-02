#  ============================================================================
#  Name        : problem_53.py
#  Description : Find how many combinatoric values of n choose k (1 <= n <= 100)
#                are greater than one million.
#  Author      : Alex Nguyen
#  Date        : December 2022
#  ============================================================================

# Import Packages
import timeit
import math

# Function
def digitSum(n):
    # Intialize
    sum = 0
    
    # Loop Over Digits
    for digit in str(n):
        sum += int(digit)
        
    return sum        

# Start Timer
start = timeit.default_timer()

# Initialize Parameters
max_sum   = -math.inf
a_max_sum = 0
b_max_sum = 0
a_max     = 100
b_max     = 100

# Compute Maximum Digital Sum
for a in range(a_max):
    for b in range(b_max):
        # Compute Digital Sum of an Expression
        digital_sum = digitSum(a**b)
        
        # Largest Digital Sum?
        if digital_sum > max_sum:
            # Save 
            max_sum   = digital_sum  
            a_max_sum = a
            b_max_sum = b      
    
# End Timer
end = timeit.default_timer()

# Print Results
print("\nMaximum digital sum value = {} (a = {}, b = {})".format(max_sum, a_max_sum, b_max_sum))
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds\n")      