# ============================================================
# PROBLEM 24 — SECOND LARGEST DISTINCT
# ============================================================
# Task:
# Find the second-largest DISTINCT element.
#
# Example:
# arr = [4, 9, 2, 9, 7]
#
# Answer:
# 7
#
# Requirements:
# - Do NOT sort.
# - Duplicate values do not count twice.
#
# Function:
# def second_largest(arr):
#     ...



def second_distinct(arr):

    largest = arr[0]

    second_largest_distinct = None

    for i in range(len(arr)):
        if arr[i] > largest :
            second_largest_distinct = largest
            largest = arr[i]

        elif arr[i] != largest and (second_largest_distinct is None or arr[i] > second_largest_distinct):
            second_largest_distinct = arr[i]


        
    return second_largest_distinct           



