# ============================================================
# VARIATION — DIFFERENCE OF SUM WITH A DIFFERENT CONDITION
# ============================================================
#
# Given N and M:
#
# Find:
#
#     sum of numbers from 1 to N that ARE divisible by M
#
#     MINUS
#
#     sum of numbers from 1 to N that are NOT divisible by M
#
# This is the REVERSE of the previous problem.
#
# Example:
#
# N = 10
# M = 3
#
# Divisible by 3:
# 3, 6, 9
# Sum = 18
#
# NOT divisible by 3:
# 1, 2, 4, 5, 7, 8, 10
# Sum = 37
#
# Answer:
#
# 18 - 37 = -19


def diffsum(n,m):


    gorup_N = 0 



   # sum of numbers from 1 to N that ARE divisible by M


    for i in range(1,n+1):
        if i % m == 0:
            gorup_N += i


    #sum of numbers from 1 to N that are NOT divisible by M

    
    group_M = 0 

    for i in range(1,m+1):
        if i % m != 0:
            group_M += i

    val = gorup_N - group_M


    return val 



