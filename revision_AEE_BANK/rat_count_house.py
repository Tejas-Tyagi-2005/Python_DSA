# ============================================================
# ARRAY REVISION — PROBLEM 1
# RAT COUNT HOUSE
# ============================================================
#
# Task:
# A rat needs `r` units of food.
#
# There are `n` houses.
# Each house contains some amount of food.
#
# Find the MINIMUM number of houses needed to provide
# at least `r` units of food for the rat.
#
# Start from the FIRST house and move from left to right.
#
# Example:
#
# arr = [2, 8, 3, 5, 4]
# r = 10
#
# Running total:
#
# House 1 → 2
# House 2 → 10  ← enough
#
# Answer:
# 2
#
#
# IMPORTANT EDGE CASES TO THINK ABOUT:
#
# 1. What if the total food in ALL houses is less than r?
#
# 2. What if r = 0?
#
# 3. What if the first house itself has enough food?
#
#
# Function:
#
# def rat_count(arr, r):
#     ...



'''
Initial self attemmpt from scratch 

Not thinking of edge cases in the initial version 

'''

def rat_count(arr,r,n):


    target_food = r * n 

    current_food = 0 

    for i in range(len(arr)):
        if current_food == target_food:
            return i 
        current_food += arr[i]
    return i 

    