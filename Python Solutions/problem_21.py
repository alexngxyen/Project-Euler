#  ============================================================================
#  Name        : problem_21.py
#  Description : Find the sum of all the amicable numbers under 10000.
#  Author      : Alex Nguyen
#  Date        : December 2022
#  ============================================================================

# Import Packages
import timeit

# Functions
def proper_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors

def amicable_pair(n):
    sum_proper_divisors = sum(proper_divisors(n))
    if sum_proper_divisors == n:
        return False
    if sum(proper_divisors(sum_proper_divisors)) == n:
        return True
    return False

# Start Timer
start = timeit.default_timer()

# Initialize Parameters
threshold            = 10**4
sum_amicable_numbers = 0

# Sum Amicable Numbers Under Threshold
sum_proper_divisors_list = []

for k in range(1, threshold + 1):
    # Sum Amicable Numbers
    if amicable_pair(k):
        sum_amicable_numbers += sum(proper_divisors(k))
      
# End Timer
end = timeit.default_timer()

# Print Results
print("\nSum of all the amicable numbers under 10000 = {}".format(sum_amicable_numbers))
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds\n")      