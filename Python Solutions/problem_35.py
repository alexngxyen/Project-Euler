#  ============================================================================
#  Name        : problem_35.py
#  Description : Find the number of circular primes below one million.
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

def rotateDigitList(n):
    # Convert Number to List
    n        = list(str(n))
    n_length = len(n)
    
    # Preallocate
    n_list = []
    
    # Loop Over Possible Digit Rotations
    for k in range(n_length):
        # Rotate Digits
        n = n[1:] + n[:1]
        
        # Convert List to Number
        n = "".join(n)
        
        # Append to List
        n_list.append(int(n))
        
    return n_list

def removeListDuplicates(n_list):
    # Preallocate
    n_list_update = []
    
    # Loop Over List
    for n in n_list:
        if n not in n_list_update:
            n_list_update.append(n)
    
    return n_list_update

# Start Timer
start = timeit.default_timer()

# Initialize Parameters
threshold_number = 10**6
count            = 0

# Compute Number of Circular Primes
k_range = list(range(2, threshold_number))
for k in k_range:
    # Compute All Possible Digit Rotations
    kth_list = rotateDigitList(k)
    
    # Find All Rotations for the k-th Number
    kth_prime_count = 0
    for digit in kth_list:
        if isPrime(digit):
            kth_prime_count += 1
    
    # Check if Circular Prime?    
    if kth_prime_count == len(kth_list):
        # Update Counter
        count += kth_prime_count
        
        # Print Counter
        print(count)
        
        # Remove Circular Primes from List
        kth_list_update = removeListDuplicates(kth_list)
        for r in range(len(kth_list_update)):
                k_range.remove(kth_list_update[r])

# End Timer
end = timeit.default_timer()

# Print Results
print("\nNumber of circular primes below {} = {}".format(threshold_number, count))
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds\n")      