#  ============================================================================
#  Name        : problem6.py
#  Description : Finds the difference between the sum of the squares of the first
#                one hundred natural numbers and the square of the sum.
#  Author      : Alex Nguyen
#  Date        : August 2022
#  ============================================================================

# Import Packages
import timeit
import numpy as np

# Start Timer
start = timeit.default_timer()

# Initialize Parameters
value = 100                                           # Number of Natural Numbers

# Sum of the Squares
sum_of_square = np.sum(np.square(np.arange(1, value + 1)))

# Square of the Sum
square_of_sum = np.square(np.sum(np.arange(1, value + 1)))

# End Timer
end = timeit.default_timer()

# Print Results
print("\nDifference between the sum of the squares and the square of the sum for", value, " natural numbers =", square_of_sum - sum_of_square)
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds\n")