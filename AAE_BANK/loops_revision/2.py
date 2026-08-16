
# ============================================================
# PROBLEM 2 — PRINT N TO 1
# ============================================================
# Task:
# Print all numbers from N down to 1.
#
# Example:
# N = 5
#
# Output:
# 5
# 4
# 3
# 2
# 1
#
# Requirement:
# Use range(start, stop, step).
#
# Function:
# def reverse_numbers(n):
#     ...


def rev_num(N):


    for i in range(N,0,-1):
        x =  print(i)

    return x
     


print(rev_num(5))
