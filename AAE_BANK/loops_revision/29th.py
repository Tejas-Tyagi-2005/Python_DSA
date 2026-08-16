# ============================================================
# PROBLEM 29 — NUMBER PATTERN
# ============================================================
# Task:
# Print the following pattern for N = 5.
#
# 1
# 12
# 123
# 1234
# 12345
#
# Requirement:
# Use nested loops.


def number_patterns(n):

    for i in range(1 , n+1):
        for j in range(i):
            print(j+1 , end="")

        print()

            

