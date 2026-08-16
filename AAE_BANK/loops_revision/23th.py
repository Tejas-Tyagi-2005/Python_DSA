
# ============================================================
# PROBLEM 22 — FIRST POSITION WHERE RUNNING SUM REACHES TARGET
# ============================================================
# Task:
# Find how many elements are needed before the running sum
# becomes greater than or equal to target.
#
# Example:
# arr = [3, 4, 2, 8]
# target = 9
#
# Running sums:
# 3
# 7
# 9  <-- stop
#
# Answer:
# 3
#
# Function:
# def first_position_sum(arr, target):
#     ...

def run(arr,target):


    running_sum = 0

    for i in range(len(arr)):                   # arr = [3, 4, 2, 8]
                                                # target = 9 
        if arr[i] != target:
            running_sum += arr[i]
        elif arr[i] == target:
            return i   

          