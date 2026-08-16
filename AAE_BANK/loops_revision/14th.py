
# ============================================================
# PROBLEM 13 — FIRST ELEMENT GREATER THAN TARGET
# ============================================================
# Task:
# Find the first element whose value is greater than target.
#
# Example:
# arr = [2, 4, 7, 3, 9]
# target = 6
#
# Answer:
# 7
#
# Requirement:
# Stop immediately after finding it.
#
# Function:
# def first_greater(arr, target):
#     ...


def first(arr,target):

    for i in range(len(arr)):
        if arr[i] > target :
            print(arr[i])
            
