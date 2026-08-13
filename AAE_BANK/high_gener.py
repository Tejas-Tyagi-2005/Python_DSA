# ============================================================
# #6 — COUNT ELEMENTS WITHIN GIVEN ABSOLUTE DIFFERENCE
# ============================================================
#
# Given an array and a target value, count how many elements
# have an absolute difference from the target that is LESS
# THAN OR EQUAL TO a given limit.
#
# Example:
#
# arr = [2, 5, 8, 10, 14]
# target = 8
# limit = 3
#
# Check each element:
#
# 2  -> |2 - 8|  = 6  -> does NOT count
# 5  -> |5 - 8|  = 3  -> counts
# 8  -> |8 - 8|  = 0  -> counts
# 10 -> |10 - 8| = 2  -> counts
# 14 -> |14 - 8| = 6  -> does NOT count
#
# Answer = 3


def maa_di_phudi(arr,target,limit):


    counts = 0 

    for i in range(len(arr)):


        if target - arr[i] <= limit and arr[i] - target <= limit:
            counts += 1

    return counts 



