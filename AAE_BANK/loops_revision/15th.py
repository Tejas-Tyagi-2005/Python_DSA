# ============================================================
# PROBLEM 14 — COUNT ELEMENTS GREATER THAN TARGET
# ============================================================
# Task:
# Count how many elements are greater than target.
#
# Example:
# arr = [2, 8, 4, 10, 3]
# target = 5
#
# Answer:
# 2
#
# Function:
# def count_greater(arr, target):
#     ...


def count(arr , target ):


     count = 0 

     for i in range(len(arr)):
          if arr[i] > target :
               count += 1
     return count 