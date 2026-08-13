#============================================================
# VARIATION 3 — SECOND-LARGEST + SMALLEST
# ============================================================
#
# Given an array of integers, return:
#
#     second-largest DISTINCT value + smallest value
#
# BUT:
#
# Ignore all negative numbers when finding the
# second-largest and smallest values.
#
# Example:
#
# arr = [4, -2, 10, 7, -8, 6]
#
# Values we actually consider:
#
# [4, 10, 7, 6]
#
# Largest = 10
# Second-largest = 7
# Smallest = 4
#
# Answer = 7 + 4 = 11


def var(arr):

    largest = None

    second_largest = None

    smallest = None 


    if arr[i] > 0 :
        if largest is None:
            largest = arr[i]
            smallest = arr[i]


    for i in range(len(arr)):
        if arr[i] > 0 and arr[i] > largest :
            second_largest = largest
            largest = arr[i]

        elif arr[i]>0 and arr[i] != largest and (second_largest is None or arr[i] > second_largest):
            second_largest = arr[i]

        if arr[i] > 0 and arr[i] < smallest:
            smallest = arr[i]

    val = second_largest +smallest


    return val 

