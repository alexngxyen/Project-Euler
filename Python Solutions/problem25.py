#  ============================================================================
#  Name        : problem25.py
#  Description : Find the index of the first term in the Fibonacci sequence to 
#                contain 1000 digits.
#  Author      : Alex Nguyen
#  Date        : August 2022
#  ============================================================================

# Import Packages
import timeit

# Start Timer
start = timeit.default_timer()

# Initialize Parameters
fibonacci_length   = 0
digit_length       = 1000

# Compute Fibonacci Index
fibonacci_number_a = 1
fibonacci_number_b = 1
fibonacci_index    = 1

while fibonacci_length < digit_length:
    # Fibonacci Sequence
    fibonacci_number_c = fibonacci_number_a + fibonacci_number_b
    fibonacci_number_a = fibonacci_number_b
    fibonacci_number_b = fibonacci_number_c
    
    # Determine Length of Fibonacci Number
    if len(str(fibonacci_number_a)) == digit_length:
        # Update Fibonacci Length
        fibonacci_length = len(str(fibonacci_number_a))
        
        # Update Fibonacci Index
        fibonacci_index += 1
        
    elif len(str(fibonacci_number_b)) == digit_length:    
        # Update Fibonacci Length
        fibonacci_length = len(str(fibonacci_number_b))
        
        # Update Fibonacci Index
        fibonacci_index += 2
        
    else:            
        # Update Fibonacci Index
        fibonacci_index    += 1

# End Timer
end = timeit.default_timer()

# Print Results
print("\nIndex of the first term in the fibonacci sequence to contain {} digits =".format(digit_length), fibonacci_index)
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds\n")      