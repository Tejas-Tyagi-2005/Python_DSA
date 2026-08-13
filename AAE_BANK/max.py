# ============================================================
# #5 — FIND MIN / MAX / SECOND MIN / SECOND MAX
# ============================================================
#
# Given an array of integers, find:
#
#     smallest
#     largest
#     second-smallest DISTINCT
#     second-largest DISTINCT
#
# Return their SUM.
#
# Example:
#
# arr = [8, 3, 12, 5, 2, 10]
#
# Smallest = 2
# Second-smallest = 3
# Largest = 12
# Second-largest = 10
#
# Answer = 2 + 3 + 12 + 10
#        = 27
#

def bigdaddy(arr):

    largest = arr[0]

    second_largest = None 

    smallest = arr[0]

    second_smallest = None 

    for i in range(1,len(arr)):

        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]

        elif arr[i] != largest and (second_largest is None or arr[i] > second_largest):
            second_largest = arr[i]

        elif arr[i] < smallest:
            second_smallest = smallest
            smallest = arr[i]

        elif arr[i] != smallest and (second_smallest is None or arr[i] < second_smallest):
            second_smallest = arr[i]

    val = largest + second_smallest + second_largest + smallest

    return val                    