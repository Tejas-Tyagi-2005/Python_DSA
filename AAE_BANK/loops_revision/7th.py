# ============================================================
# PROBLEM 7 — COUNT MULTIPLES
# ============================================================
# Task:
# Count how many numbers from 1 to N are divisible by M.
#
# Example:
# N = 20
# M = 4
#
# Answer:
# 5
#
# Function:
# def count_divisible(n, m):


def countdev(n,m):
 
     count = 0 

     for i in range(1,n+1):

        if i % m == 0:
            count +=1
     return count 

       