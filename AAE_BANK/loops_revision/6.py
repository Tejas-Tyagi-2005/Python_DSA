# ============================================================
# PROBLEM 6 — SUM OF EVEN NUMBERS
# ============================================================
# Task:
# Calculate the sum of all even numbers from 1 to N.
#
# Example:
# N = 10
#
# Answer:
# 30
#
# Function:
# def sum_even(n):
#     ...


def evensum(n):

    total = 0 


    for i in range(1,n+1):
        if i% 2 == 0:
            total += i

    return total         

