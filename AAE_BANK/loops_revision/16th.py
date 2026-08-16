# ============================================================
# LEVEL 3 — INDEX VS VALUE
# ============================================================


# ============================================================
# PROBLEM 15 — PRINT INDEXES OF EVEN ELEMENTS
# ============================================================
# Task:
# Print the INDEXES of every even element.
#
# Example:
# arr = [5, 8, 3, 10, 7, 4]
#
# Output:
# 1
# 3
# 5
#
# Important:
# Print the indexes, NOT the values.
#
# Function:
# def even_indexes(arr):
#     ...


def index(arr):

    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            print(i)
            


