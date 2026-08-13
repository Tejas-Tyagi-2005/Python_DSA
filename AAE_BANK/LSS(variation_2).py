# ============================================================
# VARIATION 2 — SECOND-LARGEST + SMALLEST
# ============================================================
#
# Given an array of integers, find:
#
#     second-largest DISTINCT value + smallest value
#
# Example:
#
# arr = [7, 2, 15, 4, 9, 15, 3]
#
# Largest = 15
# Second-largest DISTINCT = 9
# Smallest = 2
#
# Answer = 9 + 2 = 11


def var(arr):


    largest = arr[0]

    second_largest = None 

    smallest = arr[0]


    for i in range(1,len(arr)):

        if arr[i] > largest:
            second_largest = largest 
            largest = arr[i]

        elif arr[i] != largest and(second_largest is None or arr[i] > second_largest):
            second_largest = arr[i]

        if arr[i] < smallest:
            smallest = arr[i]

        val = second_largest + smallest

    return val 




