# ============================================================
# VARIATION 2 — SMALLEST PAIR WITH A CONDITION
# ============================================================
#
# Given an array of integers, find the TWO SMALLEST DISTINCT
# POSITIVE numbers and return their product.
#
# Negative numbers and zero must be ignored.
#
# Example:
#
# arr = [-5, 8, 0, 3, 2, -1, 2, 6]
#
# Valid values:
#
# [8, 3, 2, 2, 6]
#
# Smallest distinct = 2
# Second-smallest distinct = 3
#
# Answer = 2 * 3 = 6




def king(arr):



    smallest = None 

    second_smallest = None 


    if arr[i] > 0:
        if smallest is None:
            smallest = arr[i]
            second_smallest = arr[i]
        else:

            for i in range(len(arr)):
                if arr[i] < smallest:
                    second_smallest = smallest
                    smallest = arr[i]

                elif arr[i] != smallest and (second_smallest is None or arr[i] < second_smallest):
                    second_smallest = arr[i]

            val = second_smallest * smallest

            return val 

                        





            
