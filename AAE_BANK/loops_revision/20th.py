# ============================================================
# LEVEL 4 — ACCUMULATORS & CONDITIONS
# ============================================================


# ============================================================
# PROBLEM 19 — SUM POSITIVE NUMBERS
# ============================================================
# Task:
# Find the sum of all positive numbers in an array.
#
# Example:
# arr = [-2, 5, 7, -3, 4]
#
# Answer:
# 16
#
# Function:
# def positive_sum(arr):


def sum(arr):

    total = 0 

    for  i in arr:
        if i > 0:
            total += i
    return total         