#  ============================================================================
#  Name        : problem_17.py
#  Description : Find the number of letters used to write out the numbers from 
#                1 to 1000.
#  Author      : Alex Nguyen
#  Date        : August 2022
#  ============================================================================

# Import Packages
import timeit

# Function
def englishWords(n):
	if 0 <= n < 20:
		return set_one[n]
	elif 20 <= n < 100:
		return set_two[n // 10] + (set_one[n % 10] if (n % 10 != 0) else "")
	elif 100 <= n < 1000:
		return set_one[n // 100] + "hundred" + (("and" + englishWords(n % 100)) if (n % 100 != 0) else "")
	elif 1000 <= n < 1000000:
		return englishWords(n // 1000) + "thousand" + (englishWords(n % 1000) if (n % 1000 != 0) else "")


# Start Timer
start = timeit.default_timer()

# Initalize Parameters
number_threshold = 1000

set_one = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", 
           "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
set_two = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

# Compute Number of Letters
number_of_letters = sum(len(englishWords(k)) for k in range(1, number_threshold + 1))


# End Timer
end = timeit.default_timer()

# Print Results
print("\nNumber of letters from 1 to {} = {}".format(number_threshold, number_of_letters))
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds\n")      