# ============================================================
# PROBLEM 16 — PRINT INDEX AND VALUE
# ============================================================
# Task:
# Print the index and value of every positive element.
#
# Example:
# arr = [-2, 7, 4, -1]
#
# Output:
# index 1 -> value 7
# index 2 -> value 4
#
# Function:
# def positive_positions(arr):
#     ...

def indexval(arr):

    for i in range(len(arr)):

        if arr[i] > 0:
            print(i)
            print(arr[i])

