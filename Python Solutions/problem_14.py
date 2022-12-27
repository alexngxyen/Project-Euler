#  ============================================================================
#  Name        : problem_14.py
#  Description : Find a starting number under one million which produces the 
#                longest Collatz sequence.
#  Author      : Alex Nguyen
#  Date        : August 2022
#  ============================================================================

# Import Packages
import timeit

# Start Timer
start = timeit.default_timer()

# Initialize Parameters
largest_starting_number = int(1e6)
sequence_length         = 0
starting_number         = 0

# Iterate Through Numbers 
for i in range(1, largest_starting_number):  
    # Update Positive Integers
    positive_integer = i
    
    # Start Counter
    count = 1
    
    # Determine the Collatz Sequence
    while positive_integer != 1:
        if positive_integer % 2 == 0:
            # Update Even Integer
            positive_integer = positive_integer / 2
            
            # Increment Counter
            count += 1
            
        else:
            # Update Odd Integer
            positive_integer = 3*positive_integer + 1
            
            # Increment Counter
            count += 1

    # Save Values
    if count >= sequence_length:
        # Starting Number
        starting_number = i
        
        # Collatz Sequence Length
        sequence_length = count
        
# End Timer
end = timeit.default_timer()

# Print Results
print("\nStarting number, under", largest_starting_number, ", produces a Collatz sequence of length =", sequence_length, "with a starting number =", starting_number)
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds\n")            