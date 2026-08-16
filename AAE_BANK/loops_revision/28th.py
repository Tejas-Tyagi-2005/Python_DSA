
# ============================================================
# PROBLEM 28 — STAR PATTERN
# ============================================================
# Task:
# Print the following pattern for N = 5.
#
# *
# **
# ***
# ****
# *****
#
# Requirement:
# Use nested loops.
#
# Function:
# def star_pattern(n):


def star(n):

    for i in range(1 , n+1):
        for j in range(i):
            print("*" , end="")

        print()
            

            
