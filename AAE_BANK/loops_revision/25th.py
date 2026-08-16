
# ============================================================
# PROBLEM 26 — FOUR EXTREMES
# ============================================================
# Task:
# Find:
#
# - smallest
# - second-smallest DISTINCT
# - largest
# - second-largest DISTINCT
#
# Return the sum of all four values.
#
# Example:
# arr = [8, 3, 12, 5, 2, 10]
#
# Smallest = 2
# Second-smallest = 3
# Largest = 12
# Second-largest = 10
#
# Answer:
# 27
#
# Requirement:
# One traversal. Do NOT sort.
#
# Function:
# def min_max_pack(arr):
#     ..





def extreame(arr):


    largest = arr[0]

    second_largest = None 


    smallest = arr[0]

    second_smallest = None 


    for i in range(len(arr)):

        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]

        elif arr[i] != largest  and (second_largest is None or arr[i] > second_largest):
            second_largest = arr[i]


    for i in range(len(arr)):

        if arr[i] < smallest:
            second_smallest = smallest
            smallest = arr[i]

        elif arr[i] != smallest and (second_smallest is None or arr[i] < second_smallest):
            second_smallest = arr[i]


    val = largest + second_largest + smallest + second_smallest

    return val 

                        