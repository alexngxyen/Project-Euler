#  ============================================================================
#  Name        : problem_18.py
#  Description : Find the maximum total from top to bottom of a triangle.
#  Author      : Alex Nguyen
#  Date        : December 2022
#  ============================================================================

# Functions
def computeMaximumTotal(triangle):
    # Initialize Parameters
    triangle_length = len(triangle)
    maximum_value   = triangle[0][0]
    max_index       = 0
    count           = 1
    
    # Compute Maximum Total from Top to Bottom
    while count < triangle_length:

        # Update the Maximum Value
        if triangle[count][max_index] > triangle[count][max_index + 1]:
            maximum_value += triangle[count][max_index]
            max_index += 0
            
        else:
            maximum_value += triangle[count][max_index + 1]
            max_index += 1

        # Update Counter
        count += 1
                
    # Return Maximum Total
    return maximum_value

# def compute():
# 	for i in reversed(range(len(triangle) - 1)):
# 		for j in range(len(triangle[i])):
# 			triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
# 	return str(triangle[0][0])

# Import Packages
import timeit

# Start Timer
start = timeit.default_timer()

# Initalize Parameters
triangle = [  
	[75],
	[95,64],
	[17,47,82],
	[18,35,87,10],
	[20, 4,82,47,65],
	[19, 1,23,75, 3,34],
	[88, 2,77,73, 7,63,67],
	[99,65, 4,28, 6,16,70,92],
	[41,41,26,56,83,40,80,70,33],
	[41,48,72,33,47,32,37,16,94,29],
	[53,71,44,65,25,43,91,52,97,51,14],
	[70,11,33,28,77,73,17,78,39,68,17,57],
	[91,71,52,38,17,14,91,43,58,50,27,29,48],
	[63,66, 4,68,89,53,67,30,73,16,69,87,40,31],
	[ 4,62,98,27,23, 9,70,98,73,93,38,53,60, 4,23],
]

# Compute Maximum Total from Top to Bottom
# print(computeMaximumTotal(triangle))
# print(compute())

# End Timer
end = timeit.default_timer()

# Print Results
# print("\nNumber of letters from 1 to {}".format(numbers))
print("Elapsed time =", str.format('{0:.15f}', end - start), "seconds\n")      
