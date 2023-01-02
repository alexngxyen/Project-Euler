#  ============================================================================
#  Name        : problem_45.py
#  Description : Find the triangle number which is also a pentagonal and hexagonal
#                number.
#  Author      : Alex Nguyen
#  Date        : December 2022
#  ============================================================================

# Import Packages
import timeit

# Functions
def triangle_numbers(n):
    return n*(n + 1) // 2

def pentagonal_numbers(n):
    return n*(3*n - 1) // 2

def hexagonal_numbers(n):
    return n*(2*n - 1)

# Start Timer
start = timeit.default_timer()

# Initialize Parameters
sequence_length   = 10**5
shared_value_list = []
triangle_list     = [triangle_numbers(n) for n in range(1, sequence_length + 1)]
pentagon_list     = [pentagonal_numbers(n) for n in range(1, sequence_length + 1)]
hexagon_list      = [hexagonal_numbers(n) for n in range(1, sequence_length + 1)]

# Find Triangle Number That is Also a Pentagonal and Hexagonal Number
for k in range(sequence_length):
    if triangle_list[k] in pentagon_list and triangle_list[k] in hexagon_list:
        shared_value_list.append(triangle_list[k])

# End Timer
end = timeit.default_timer()

# Print Results
print("\nList of triangle numbers that are also pentagonal and hexagonal = {} ".format(shared_value_list))
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds\n")      