#  ============================================================================
#  Name        : problem7.py
#  Description : Finds the 1001st prime number.  
#  Author      : Alex Nguyen
#  Date        : August 2022
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
number_of_primes = 10001                                 # Number of Prime Numbers
prime_numbers    = []                                    # List of Prime Numbers
count            = 1                                     # Counter

# Determine Prime Numbers
while len(prime_numbers) < number_of_primes + 1:
    # Check If Natural Number is Prime
    if isPrime(count):
        # Add number to list of prime numbers
        prime_numbers.append(count)
    
    # Update Counter
    count += 1

# End Timer
end = timeit.default_timer()

# Print Results
print("\n", number_of_primes, "prime number =", prime_numbers[-1])
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds\n")