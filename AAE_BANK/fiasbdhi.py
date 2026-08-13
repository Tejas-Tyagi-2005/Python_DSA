#============================================================
# #4 — SECOND LARGEST ELEMENT
# ============================================================
#
# Given an array of integers, return the SECOND-LARGEST
# DISTINCT element.
#
# Example:
#
# arr = [4, 7, 2, 9, 9, 5]
#
# Largest = 9
# Second-largest DISTINCT = 7
#
# Answer = 7



def fjh(arr):

    largest = arr[0]

    second_largest = None 

    for i in range(1,len(arr)):
        if arr[i] > largest:
            second_largest = largest 
            largest = arr[i]

        elif arr[i] != largest and (second_largest is None or arr[i] > second_largest):
            second_largest = arr[i]

    return second_largest

