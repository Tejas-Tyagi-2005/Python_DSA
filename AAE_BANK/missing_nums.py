# ============================================================
# #8 — MISSING NUMBER IN 1...N
# ============================================================
#
# You are given an array containing numbers from 1 to N,
# but exactly ONE number is missing.
#
# Return the missing number.
#
# Example:
#
# arr = [1, 2, 3, 5]
# n = 5
#
# Expected numbers:
# 1, 2, 3, 4, 5
#
# Missing = 4
#
# ------------------------------------------------------------


'''
a pretty high gener question for a low gener but imma try anyways 

'''

def missing(arr , N):

    expected_sum = 0

    for i in range(1,N+1):
        expected_sum += i

    
    actual_sum = 0
    
    for i in arr:
        actual_sum += i 



    expect_num = expected_sum - actual_sum

    return expected_sum











   