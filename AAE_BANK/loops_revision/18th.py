# ============================================================
# PROBLEM 17 — FIRST OCCURRENCE
# ============================================================
# Task:
# Find the index of the first occurrence of target.
#
# Example:
# arr = [4, 7, 2, 7, 9]
# target = 7


def target(arr,target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i
