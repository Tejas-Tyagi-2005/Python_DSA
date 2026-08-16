# ============================================================
# PROBLEM 27 — THIRD LARGEST DISTINCT
# ============================================================
# Task:
# Find the third-largest DISTINCT element.
#
# Example:
# arr = [4, 9, 2, 9, 7, 6]
#
# Largest = 9
# Second-largest = 7
# Third-largest = 6
#
# Answer:
# 6
#
# Requirements:
# - Do NOT sort.
# - Duplicate values do not count twice.
#
# Function:
# def third_largest(arr):
#     ...



def third(arr):


    largest = arr[0]

    second_largest = None

    third_largest = None 


    for i in range(len(arr)):
        if arr[i] > largest:
            third_largest = second_largest
            second_largest = largest
            largest = arr[i]

        elif  arr[i] != largest and (second_largest is None or arr[i] > second_largest):
            third_largest = second_largest
            second_largest = arr[i]


        elif arr[i] != second_largest and arr[i] != largest and  (third_largest is None or arr[i] > third_largest):
                    third_largest = arr[i]    

    return third_largest


