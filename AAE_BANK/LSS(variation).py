# ============================================================
# VARIATION 1 — SECOND SMALLEST + LARGEST
# ============================================================
#
# Given an array of integers, find:
#
#     second-smallest + largest
#
# Example:
#
# arr = [8, 3, 12, 5, 2, 10]
#
# Smallest = 2
# Second-smallest = 3
# Largest = 12
#
# Answer = 3 + 12 = 15



def variation(arr):

    largest = arr[0]

    smallest = arr[0]

    second_smallest = None 


    for i in range(1,len(arr)):
        if arr[i] < smallest:
            second_smallest = smallest
            smallest = arr[i]

        elif arr[i] != smallest and ( second_smallest is None or arr[i] < second_smallest):
            second_smallest = arr[i]


        if arr[i] > largest:
            largest = arr[i]

    val = second_smallest + largest

    return val 

                




