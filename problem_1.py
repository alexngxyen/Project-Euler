# Import Packages
import timeit

# Start Timer
start = timeit.default_timer()

# Initalize Parameters
value        = 1000                                 # Value of Interest
count        = 1                                    # Number of Iterations
sum          = 0                                    # Sum of Multiples
multiple_one = 3
multiple_two = 5

while (count < value):
    if count % multiple_one == 0 or count % multiple_two == 0:
        sum += count

    # Update Counter
    count += 1

# End Timer
end = timeit.default_timer()

# Print Results
print("Sum of all the multiples of", multiple_one, "or", multiple_two, "below", value, "=", sum)
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds")