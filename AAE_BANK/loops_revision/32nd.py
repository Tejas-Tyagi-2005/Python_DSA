# ============================================================
# PROBLEM 32 — LONGEST SAME-VALUE STREAK
# ============================================================
# Task:
# Find the longest consecutive streak of the same value.
#
# Example:
#
# arr = [1, 1, 1, 2, 2, 5, 5, 5, 5, 3]
#
# Answer:
# 4
#
# Because:
#
# 5, 5, 5, 5
#




def same_streak(arr):


    streak_lenght = 1 # start with 1 , becasue one element in itself is a streak 

    best_streak = 1


    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            streak_lenght += 1

        elif arr[i] != arr[i+1]:
            if streak_lenght > best_streak:
                best_streak = streak_lenght
            streak_lenght = 1



    if streak_lenght > best_streak:
        best_streak = streak_lenght      

              
    return best_streak



            