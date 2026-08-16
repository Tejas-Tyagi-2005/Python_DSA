# ============================================================
# PROBLEM 4 — PRINT ODD NUMBERS BACKWARDS
# ============================================================
# Task:
# Print all odd numbers from N down to 1.
#
# Example:
# N = 9
#
# Output:
# 9
# 7
# 5
# 3
# 1
#

def odddown(n):

    for i in range(n , 0 , -1):
        if i % 2 != 0:
            print(i)

            


