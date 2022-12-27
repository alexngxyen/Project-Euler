#  ============================================================================
#  Name        : problem_57.py
#  Description : Find how many fractions contain a numerator with more digits 
#                than the denominator for the suare root of two expressed as an 
#                infinite coninued fraction.   
#  Author      : Alex Nguyen
#  Date        : December 2022
#  ============================================================================

# Import Packages
import timeit
import sympy as sp

# Functions
def squareRootOfTwoTerm(kth_term):
    # Initialize 
    square_root_terms = sp.Rational(1, 2)

    # Compute Term
    for k in range(kth_term):
        square_root_terms = 1/(2 + square_root_terms)
        
    return sp.simplify(1 + square_root_terms)


# Start Timer
start = timeit.default_timer()

# Initialize Parameters
number_of_terms = 1000
count           = 0

# Compute Each Term of the Infinite Series Expression
for k in range(number_of_terms):
    # k-th Term
    square_root_of_two_terms = squareRootOfTwoTerm(k)
    
    # Numerator and Denominator
    numerator, denominator = sp.fraction(square_root_of_two_terms)
    
    # Number of Digits in Numerator Bigger than Denominator?
    if len(str(numerator)) > len(str(denominator)):
        count += 1
    
# End Timer
end = timeit.default_timer()

# Print Results
print("\nNumber of times the digits in the numerator are greater than the digits in the denominator = {}".format(count))
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds\n")      