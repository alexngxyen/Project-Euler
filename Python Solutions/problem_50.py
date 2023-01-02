#  ============================================================================
#  Name        : problem_50.py
#  Description : Find the largest prime below one million that can be written as
#                the sum of the most consecutive primes.
#  Author      : Alex Nguyen
#  Date        : December 2022
#  ============================================================================

# Import Packages
import timeit

# Functions
def isPrime(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

# Start Timer
start = timeit.default_timer()

# Initialize Parameters
prime_threshold = 10**2
max_prime_value = 0

# Compute List of Primes Below Threshold
prime_list = []
for k in range(2, prime_threshold + 1):
    if isPrime(k):
        prime_list.append(k) 

# Find Prime with the Most Consecutive Primes as its Sum
for k in range(len(prime_list)):
    prime_sum = 0
    for j in range(len(prime_list[:k])):
        prime_sum += prime_list[j]
        if prime_sum > prime_threshold:
            break
        if prime_sum == prime_list[k]:
            if prime_sum > max_prime_value:
                max_prime_value = prime_sum

print(max_prime_value)
# print(prime_list)

# End Timer
end = timeit.default_timer()

# Print Results
# print("\nPrime with the most consecutive primes as its sum = {}".format())
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds\n")      