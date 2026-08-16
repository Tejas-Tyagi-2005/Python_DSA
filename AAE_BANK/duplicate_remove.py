# ============================================================
# PROBLEM 10 — REMOVE DUPLICATES FROM AN ARRAY
# ============================================================
# Task:
# Remove duplicate values from an array.
#
# Keep only the FIRST occurrence of each value.
#
# Example:
#
# arr = [4, 2, 4, 7, 2, 9, 7]
#
# Answer:
# [4, 2, 7, 9]


def remove_dups(arr):

    unique_arr = []

    seen = []

    for i in range(len(arr)):

        if arr[i] not  in seen:
            unique_arr.append(arr[i])
            seen.append(arr[i])
            
    return unique_arr
               


