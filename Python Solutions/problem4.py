#  ============================================================================
#  Name        : problem4.py
#  Description : Finds the largest palindrome made from the product of two 
#                3-digit numbers.  
#  Author      : Alex Nguyen
#  Date        : August 2022
#  ============================================================================

# Import Packages
import timeit

# Start Timer
start = timeit.default_timer()

# Initialize Parameters
digits          = 3                                   # Number of Digits
i_range         = 10**digits                          # One Range of Values 
j_range         = i_range                             # Another Range of Values
palindrome_list = []                                  # List to Store Palindromes

for i in range(i_range // 10, i_range):
    for j in range(j_range // 10, j_range):
        # Multiply i and j Together
        product = i * j

        # Determine if the Product is Palindrome number
        product_string = str(product)

        if product_string == product_string[::-1]:
            palindrome_list.append(int(product_string))


# End Timer
end = timeit.default_timer()

# Print Results
print("Largest palindrome made from the product of two", digits, "digit numbers =", max(palindrome_list))
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds")