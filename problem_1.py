import math

# Initalize Parameters
value        = 1000                                 # Value of Interest
count        = 1                                    # Number of Iterations
sum          = 0                                    # Sum of Multiples
multiple_one = 3
multiple_two = 5

while (count < value):
    if count % 3 == 0 or count % 5 == 0:
        sum += count

    # Update Counter
    count += 1

print(sum)