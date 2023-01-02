#  ============================================================================
#  Name        : problem_55.py
#  Description : Find the number of Lychrel numbers below 10,000.
#  Author      : Alex Nguyen
#  Date        : December 2022
#  ============================================================================

# Import Packages
import timeit

# Functions
def is_palindrome(n):
    return str(n) == str(n)[::-1]

def lychrel_number(n):
    # Initialize
    count = 1
    
    while count <= 50:
        # Check if Palindrome
        n += int(str(n)[::-1])
        if is_palindrome(n):
            # Not Lychrel Number
            return False
        
        # Update Counter
        count += 1  
    # Lychrel Number
    return True


# Start Timer
start = timeit.default_timer()

# Initialize Parameters
sequence_length = 10**4
count           = 0

# Compute the Number of Lychrel Numbers
for k in range(1, sequence_length + 1):
    if lychrel_number(k):
        count += 1

# End Timer
end = timeit.default_timer()

# Print Results
print("\nNumber of Lychrel numbers below ten-thousand = {} ".format(count))
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds\n")      