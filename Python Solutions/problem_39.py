#  ============================================================================
#  Name        : problem_39.py
#  Description : Find the value of p <= 1000 for which the number of solutions
#                is maximized.
#  Author      : Alex Nguyen
#  Date        : January 2023
#  ============================================================================

# Import Packages
import timeit

# Start Timer
start = timeit.default_timer()

# Initialize Parameters
perimeter_threshold      = 1000
count                    = 0
perimeter_solution_index = 0
number_of_solutions      = 0
perimeter_solution      = [] 

# Compute the Possible Perimeter Solutions for a Given "p" Value
while count <= perimeter_threshold:
    # Preallocate
    a_potential   = []
    b_potential   = []
    c_potential   = []
    abc_potential = []

    for a in range(1, count + 1):
        for b in range(1, count + 1):
            # Pythagorean Theorem 
            c = (a**2 + b**2)**0.5
            
            # Perimeter
            side_lengths = [a, b, c]
            perimeter    = sum(side_lengths)
            
            # Check
            if perimeter == count and a not in b_potential and b not in a_potential:
                # Save Individual Side Lengths
                a_potential.append(a)
                b_potential.append(b)
                c_potential.append(c)
                
                # Save Grouped Side Lengths
                abc_potential.append([int(a), int(b), int(c)])
    
    # Save Perimeter with the Most Solutions
    if len(a_potential) >= number_of_solutions:
        number_of_solutions      = len(a_potential)
        perimeter_solution       = abc_potential
        perimeter_solution_index = count
    
    # Update Counter
    count +=1

print((perimeter_solution))

# End Timer
end = timeit.default_timer()

# Print Results
print("\nValue of p <= {} with the number of solutions maximized = {} ({} # of solutions)".format(perimeter_threshold, perimeter_solution_index, number_of_solutions))
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds\n")      