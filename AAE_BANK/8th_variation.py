# ============================================================
# VARIATION — MISSING NUMBER, UNSORTED ARRAY
# ============================================================
#
# You are given an array containing numbers from 1 to N,
# with exactly ONE number missing.
#
# The array is NOT sorted.
#
# Find the missing number.
#
# Example:
#
# arr = [7, 3, 1, 6, 5, 2]
# N = 7
#
# Expected:
# 1, 2, 3, 4, 5, 6, 7
#
# Missing = 4
#
# ------------------------------------------------------------

def mdf(arr,n):

    expected_sum = 0
    actual_sum = 0


    for i in range(1,n+1):
        expected_sum += i 

    for i in arr:
        actual_sum += i    

    bla = expected_sum - actual_sum

    return bla 

    