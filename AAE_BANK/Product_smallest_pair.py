# ============================================================
# #3 — PRODUCT OF SMALLEST PAIR
# ============================================================
#
# Given an array of integers, find the TWO SMALLEST elements
# and return their product.
#
# Example:
#
# arr = [8, 3, 12, 5, 2, 10]
#
# Smallest = 2
# Second-smallest = 3
#
# Answer = 2 * 3 = 6



def POSP(arr):         # [9,4,3,6]  --> 4*3 = 12 

    smallest = arr[0]   

    second_smallest = None 

    for i in range(len(arr)):

        if arr[i] < smallest:
            second_smallest = smallest
            smallest = arr[i]

        elif second_smallest is None or arr[i] < second_smallest:
            second_smallest = arr[i]


    val = smallest * second_smallest

    return val 



