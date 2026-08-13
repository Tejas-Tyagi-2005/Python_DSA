# ============================================================
# #7 — DIFFERENCE OF SUM
# ============================================================
#
# Given two integers N and M:
#
# Find:
#
#     sum of numbers from 1 to N that are NOT divisible by M
#
#     MINUS
#
#     sum of numbers from 1 to N that ARE divisible by M
#
# Example:
#
# N = 10
# M = 3
#
# Numbers from 1 to 10 divisible by 3:
#
# 3, 6, 9
#
# Divisible sum = 18
#
# Numbers NOT divisible by 3:
#
# 1, 2, 4, 5, 7, 8, 10
#
# Non-divisible sum = 37
#
# Answer = 37 - 18 = 19



# since the questrion just says number 1 so we are gonna assume it literally means numeber 1 and not arr[1]
# no mention of arrary in the question so none assumed 


def diffSum(n ,m ):


    #sum of numbers from 1 to N that are NOT divisible by M

    # I need to travere from numbers 1 to n . how do I do that without using an array since none is given ?

    
    group_N = 0

    for i in range(1,n+1): # attempted to invent syntax to traverse from 1 to n 
        if i % m != 0 :
            group_N += i


    
    #sum of numbers from 1 to N that ARE divisible by M

    group_M = 0 

    for i in range(1,n+1):
        if i % m == 0:
            group_M+= i
    val = group_N - group_M


    return val         





