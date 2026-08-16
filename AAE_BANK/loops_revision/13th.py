
# ============================================================
# PROBLEM 12 — COUNT POSITIVE NUMBERS
# ============================================================
# Task:
# Count how many positive numbers are present in an array.
#
# Example:
# arr = [-3, 4, 0, 7, -2, 9]
#
# Answer:
# 3
#
# Function:
# def count_positive(arr):


def posc(arr):

    count = 0 

    for i in range(len(arr)):
        if arr[i] > 0:
            count += 1 

    return count 

        