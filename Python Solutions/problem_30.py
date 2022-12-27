#  ============================================================================
#  Name        : problem_30.py
#  Description : Find the sum of all the numbers that can be written as the sum
#                of fifth powers of their digits.   
#  Author      : Alex Nguyen
#  Date        : December 2022
#  ============================================================================

# Import Packages
import timeit

# Start Timer
start = timeit.default_timer()

# Initialize Parameters
number_of_digits = 5
digit_sum_list   = []

# Compute Numbers Written as the Sum of Fifth Power of Their Digits
for k in range(2, 10**7): 
    # Intialize
    sum_of_powers = 0
    
    # Loop Over Digits
    for digit in str(k):
        sum_of_powers += int(digit)**number_of_digits
        
    # Check if Sum of Powers is Equal to k
    if sum_of_powers == k:
        digit_sum_list.append(k)

# End Timer
end = timeit.default_timer()

# Print Results
print("\nSum of all the numbers that can be written as the sum of fifth powers of their digits = {} (Digit Sum List: {})".format(sum(digit_sum_list), digit_sum_list))
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds\n")      