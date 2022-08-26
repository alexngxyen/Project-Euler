#  ============================================================================
#  Name        : problem15.py
#  Description : Finds the number of routes to move from the top left corner to 
#                the bottom right corner of a 20 x 20 grid.  
#  Author      : Alex Nguyen
#  Date        : August 2022
#  ============================================================================

# Import Packages
import timeit
import math

# Start Timer
start = timeit.default_timer()

# N Choose K Selection Problem
grid_size = 20                                                                      # Grid Size
n         = 2 * grid_size
k         = grid_size

# Determine Number of Routs
number_of_routes = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

# End Timer
end = timeit.default_timer()

# Print Results
print("\nNumber of routes from top left corner to bottom right corner in a", grid_size, "x", grid_size, "=", number_of_routes)
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds\n")