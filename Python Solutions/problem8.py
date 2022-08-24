# ============================================================================
#  Name        : problem8.py
#  Description : Finds the thirteen adjacent digits in the 1000-digit number that
#                have the greatest product.
#  Author      : Alex Nguyen
#  Date        : August 2022
#  ============================================================================

# Import Packages
import timeit

# Function
def greatestProductOfAdjacentDigits(number, number_of_digits):
    # Initialize Parameters
    greatest_product = 0
    product          = 1
    index            = 0
    
    # Find Greatest Product
    while index + number_of_digits <= len(number):
        # Update Product
        for i in range(number_of_digits):
            product *= int(number[index + i])
        
        # Update Greatest Product
        if product > greatest_product:
            greatest_product = product
        
        # Update Product
        product = 1
        
        # Update Index
        index += 1
    
    # Return Greatest Product
    return greatest_product

# Start Timer
start = timeit.default_timer()

# Initialize Parameters
one_thousand_digit_number = str(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)
adjacent_digits           = 13

# Find Greatest Product of Adjacent Digits
greatest_product = greatestProductOfAdjacentDigits(one_thousand_digit_number, adjacent_digits)

# End Timer
end = timeit.default_timer()

# Print Results
print("The", adjacent_digits, "adjacent digits in the 1000-digit number which have the greatest product =", greatest_product)
print("Elapsed time =", str.format('{0:.15f}',end - start), "seconds")