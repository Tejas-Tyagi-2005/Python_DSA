#============================================================
# VARIATION 4 — SECOND-LARGEST + SMALLEST
# ============================================================
#
# Given an array of integers, find:
#
#     second-largest DISTINCT value + smallest value
#
# This time, the array can contain DUPLICATES.
#
# Example:
#
# arr = [6, 3, 12, 12, 8, 3, 5]
#
# Largest = 12
# Second-largest DISTINCT = 8
# Smallest = 3
#
# Answer = 8 + 3 = 11



# We have not covered the second_largest DUPLICATE versino , but im gonna give it a try 



def LSS(arr):

    largest = arr[0]

    second_largest = None 

    Third_largest = None 

    smallest = arr[0]

    for i in range(1,len(arr)):

        if arr[i] > largest:
            Third_largest = second_largest
            second_largest = largest
            largest = arr[i]

        elif arr[i] != largest and (second_largest is None or arr[i] > second_largest):
            Third_largest = second_largest
            second_largest = arr[i]

        elif arr[i] != second_largest and (Third_largest is None or arr[i] > Third_largest):
            Third_largest = arr[i]


        if arr[i] < smallest:
            smallest = arr[i]

    val = smallest + second_largest

    return val 


