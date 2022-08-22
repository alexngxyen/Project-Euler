# Import Packages
import timeit
import math

# Start Timer
start = timeit.default_timer()

# Initialize Parameters
value = 20                                           # Value of Interest

# Determine Least Common Multiple
num = math.lcm(*range(1, value + 1))

# End Timer
end = timeit.default_timer()

# Print Results
print("Smallest positive number divisible by all numbers from 1 to", value, "=", num)
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds")