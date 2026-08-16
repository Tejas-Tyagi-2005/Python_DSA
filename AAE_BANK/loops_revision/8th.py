# ============================================================
# LEVEL 2 — ARRAY TRAVERSAL
# ============================================================


# ============================================================
# PROBLEM 8 — FIND LARGEST ELEMENT
# ============================================================
# Task:
# Find the largest element in an array.
#
# Do NOT use max().
#
# Example:
# arr = [4, 8, 2, 11, 5]
#
# Answer:
# 11
#
# Function:
# def largest(arr)


def largest(arr):

    largest = arr[0]

    for i in range(len(arr)):
        if arr[i]>largest:
            largest = arr[i]

    return largest

        