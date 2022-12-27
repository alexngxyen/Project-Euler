#  ============================================================================
#  Name        : problem_31.py
#  Description : Find the number of different ways 2 pounds can be made using 
#                any number of coins from the available coins
#  Author      : Alex Nguyen
#  Date        : December 2022
#  ============================================================================

# Import Packages
import timeit

# Start Timer
start = timeit.default_timer()

# Initialize Parameters
eight_coins     = [1, 2, 5, 10, 20, 50, 100, 200]
one_pound_count = 200
two_pound_count = 100
five_pound_count = 40
ten_pound_count = 20
twenty_pound_count = 10
fifty_pound_count = 4
one_hundred_pound_count = 2
two_hundred_pound_count = 1
count                   = 0

# Compute Different Permutations to Get 2 Pounds
for one in range(one_pound_count + 1):
    for two in range(two_pound_count + 1):
        for five in range(five_pound_count + 1):
            for ten in range(ten_pound_count + 1):
                for twenty in range(twenty_pound_count + 1):
                    for fifty in range(fifty_pound_count + 1):
                        for hundred in range(one_hundred_pound_count + 1):
                            for two_hundred in range(two_hundred_pound_count + 1):
                                
                                # Check if Sum of Coins is 2 Pounds
                                if one*1 + two*2 + five*5 + ten*10 + twenty*20 + fifty*50 + hundred*100 + two_hundred*200 == 200:
                                    count += 1

# End Timer
end = timeit.default_timer()

# Print Results
print("\nNumber of different ways to obtain two pounds = {}".format(count))
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds\n")      