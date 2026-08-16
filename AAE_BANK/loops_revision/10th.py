# ============================================================
# PROBLEM 10 — SUM ARRAY ELEMENTS
# ============================================================
# Task:
# Calculate the sum of all elements in an array.
#
# Do NOT use sum().
#
# Example:
# arr = [4, 8, 2, 11]
#
# Answer:
# 25
#
# Function:
# def array_sum(arr):
#     ...


def sum(arr):

    total = 0 

    for  i in range(len(arr)):
        total += i 
    return total 

    
