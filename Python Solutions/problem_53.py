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

# Start Timer
start = timeit.default_timer()

# Initialize Parameters
max_n_value = 100
count       = 0

# Compute N Choose K Values Greater Than One Million
for n in range(1, max_n_value + 1):
    for r in range(1, n + 1):
        # Compute N Choose K Value
        n_choose_k = math.comb(n, r)

        # Check if N Choose K Value is Greater Than One Million
        if n_choose_k > 1e6:
            count += 1
    
# End Timer
end = timeit.default_timer()


# Print Results
print("\nNumber of times the n choose k value is greater than one million = {}".format(count))
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds\n")      