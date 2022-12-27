#  ============================================================================
#  Name        : problem_48.py
#  Description : Find the last ten digits of the series 1^1 + 2^2 + ... + 1000^1000
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
length_of_series = 1000
series_sum       = 0                 

# Compute Sum of Series
for k in range(1, length_of_series + 1):  
    # k-th Element of the Series
    series_sum += k**k
    
# Last Ten Digits
series_sum_digits = str(series_sum)[-10:]
    
# End Timer
end = timeit.default_timer()

# Print Results
print("\nLast ten digits of the series = {}".format(series_sum_digits))
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds\n")      