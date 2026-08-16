# ============================================================
# PROBLEM 21 — DIFFERENCE OF EVEN AND ODD SUMS
# ============================================================
# Task:
# Find:
#
# sum of even elements - sum of odd elements
#
# Example:
# arr = [2, 5, 4, 7]
#
# Even sum = 6
# Odd sum  = 12
#
# Answer:
# -6
#
# Function:
# def even_odd_difference(arr):
#     ...


def hapuyu(arr):

    total_uno = 0 
    total_muno = 0

    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            total_uno += arr[i]

    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            total_muno += arr[i]

    val = total_uno - total_muno
    return val                