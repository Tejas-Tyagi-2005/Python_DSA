# ============================================================
# PROBLEM 18 — COUNT OCCURRENCES
# ============================================================
# Task:
# Count how many times target occurs in an array.
#
# Example:
# arr = [2, 5, 2, 7, 2, 9]
# target = 2
#
# Answer:
# 3
#
# Function:
# def count_occurrences(arr, target):


def count(arr,target):


    count = 0 

    for i in range(len(arr)):
        if arr[i] == target:
            count += 1 
    return count         