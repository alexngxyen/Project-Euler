#  ============================================================================
#  Name        : problem_29.py
#  Description : Find the number of distnct terms in the sequence generated by
#                a^b for 2 <= a <= 100 and 2 <= b <= 100.
#  Author      : Alex Nguyen
#  Date        : January 2023
#  ============================================================================

# Import Packages
import timeit

# Start Timer
start = timeit.default_timer()

# Initialize Parameters
a_max       = 100
b_max       = 100
ab_sequence = []

# Generate Sequence
for a in range(2, a_max + 1):
    for b in range(2, b_max + 1):
        # Save Exponential Value
        ab_sequence.append(a**b)

# Find Number of Distinct Terms
ab_sequence = sorted(set(ab_sequence))

# End Timer
end = timeit.default_timer()

# Print Results
print("\nNumber of distinct terms in the sequence a**b = {} with a_max, b_max = {}, {}".format(len(ab_sequence), a_max, b_max))
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds\n")      