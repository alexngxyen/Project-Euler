#  ============================================================================
#  Name        : problem_17.py
#  Description : Find the number of letters used to write out the numbers from 
#                1 to 1000.
#  Author      : Alex Nguyen
#  Date        : August 2022
#  ============================================================================

# Import Packages
import numbers
import timeit

# Start Timer
start = timeit.default_timer()

# Initalize Parameters
numbers = 1000


# End Timer
end = timeit.default_timer()

# Print Results
print("\nNumber of letters from 1 to {}".format(numbers))
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds\n")      
