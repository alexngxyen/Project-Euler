#  ============================================================================
#  Name        : problem2.py
#  Description : Finds the sum of the even-valued fibonacci sequence terms whose
#                values do not exceed four million.
#  Author      : Alex Nguyen
#  Date        : August 2022
#  ============================================================================

# Import Packages
import timeit

# Start Timer
start = timeit.default_timer()

# Initialize Parameters
value                = 4e6                   # Value of Interest
fibonacci_number_one = 1                     # First Fibonacci Number
fibonacci_number_two = 2                     # Second Fibonacci Number
sum_one              = 0                     # Sum of Even-Valued Fibonacci One Numbers
sum_two              = 0                     # Sum of Even-Valued Fibonacci Two Numbers

while fibonacci_number_one < value or fibonacci_number_two < value:
    # Even-Valued First Fibonacci Number
    if fibonacci_number_one % 2 == 0:
        sum_one += fibonacci_number_one

    # Even-Valued Second Fibonacci Number
    elif fibonacci_number_two % 2 == 0:
        sum_two += fibonacci_number_two

    # Update the Fiboacci Numbers
    fibonacci_number_one = fibonacci_number_one + fibonacci_number_two
    fibonacci_number_two = fibonacci_number_one + fibonacci_number_two

# End Timer
end = timeit.default_timer()

# Print Results
print("Sum of all the even-valued fibonacci terms =", sum_one + sum_two)
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds")