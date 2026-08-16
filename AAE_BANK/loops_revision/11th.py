
# ============================================================
# PROBLEM 11 — COUNT EVEN ELEMENTS
# ============================================================
# Task:
# Count how many even numbers are present in an array.
#
# Example:
# arr = [3, 4, 7, 8, 10]
#
# Answer:
# 3
#
# Function:
# def count_even(arr):
#     ...


def even_count(arr):

    count = 0 

    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            count += 1 
    return count 
         
