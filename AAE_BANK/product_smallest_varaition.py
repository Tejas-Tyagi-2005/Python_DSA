# ============================================================
# VARIATION — TWO SMALLEST DISTINCT VALUES
# ============================================================
#
# Given an array of integers, find the TWO SMALLEST DISTINCT
# values and return their product.
#
# Example:
#
# arr = [8, 3, 2, 2, 5, 3]
#
# Smallest distinct = 2
# Second-smallest distinct = 3
#
# Answer = 2 * 3 = 6



def abd(arr):

    smallest = arr[0]

    second_smallest = None 

    for i in range(1 , len(arr)):

        if arr[i] < smallest:
            second_smallest = smallest
            smallest = arr[i]

        elif arr[i] != smallest and (second_smallest is None or arr[i] < second_smallest):
            second_smallest = arr[i]

    val = smallest * second_smallest

    return val 

            

    




