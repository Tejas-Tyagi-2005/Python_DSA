# ============================================================
# PROBLEM 9 — FIND SMALLEST ELEMENT
# ============================================================
# Task:
# Find the smallest element in an array.
#
# Do NOT use min().
#
# Example:
# arr = [4, 8, 2, 11, 5]
#
# Answer:
# 2
#
# Function:
# def smallest(arr):


def small(arr):

    smallest = arr[0]

    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
    return smallest

        