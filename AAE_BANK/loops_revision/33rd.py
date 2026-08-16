# ============================================================
# PROBLEM 33 — LONGEST INCREASING CONSECUTIVE STREAK
# ============================================================
# Task:
# Find the longest consecutive streak where every element
# is greater than the previous element.
#
# Example:
#
# arr = [1, 2, 3, 2, 4, 5, 6, 1]
#
# Streaks:
#
# 1, 2, 3       -> 3 elements
# 2, 4, 5, 6    -> 4 elements
#
# Answer:
# 4
#

def streak(arr):

    current_streak = 1


    best_streak = 1 


    for i in range(len(arr)-1):

        if arr[i] < arr[i+1]:
            current_streak += 1
            
        else :
            if current_streak > best_streak:
                best_streak = current_streak
                
                
    if current_streak > best_streak:
        best_streak = current_streak

    return best_streak                 



