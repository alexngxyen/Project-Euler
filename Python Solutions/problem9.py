#  ============================================================================
#  Name        : problem9.py
#  Description : Finds the pythagorean triplet (a set of three natural numbers 
#                a < b < c for which a**2 + b**2 = c**2) for which a + b + c = 
#                1000.
#  Author      : Alex Nguyen
#  Date        : August 2022
#  ============================================================================

# Import Packages
import timeit

# Start Timer
start = timeit.default_timer()

# Initialize Parameters
value = 1000                               # Constraint on Pythagorean Triplet 

# Determine Pytagorean Triplet Values
for a in range(1, value):
    for b in range(1, value):
         # Apply Pythagorean Triplet Constraint
         c = value - (a + b)
         
         # Determine if a Pythagorean Triplet
         if a**2 + b**2 == c**2:
            # Product of the Pythagorean Triplet Values    
            triplet_product = a * b * c
            a_triplet       = a
            b_triplet       = b
            c_triplet       = c
        
# End Timer 
end = timeit.default_timer()

# Print Results
print("\nPythagorean triplet values are", a_triplet, ",", b_triplet, ",", c_triplet, "with the product =", triplet_product)
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds\n")