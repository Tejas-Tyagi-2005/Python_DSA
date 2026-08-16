# ============================================================
# #9 — ROTATE ARRAY LEFT BY K
# ============================================================
#
# Given an array and an integer K, rotate the array to the LEFT
# by K positions.
#
# Example:
#
# arr = [1, 2, 3, 4, 5]
# k = 2
#
# Result:
#
# [3, 4, 5, 1, 2]
#
# ------------------------------------------------------------


# powering up low gener.exe 


def ferdinand(arr,k):

    golo = []

    for i in range(k+1 , len(arr)):
        golo.append(arr[i])


    for i in arr:
        if i <= k:
            golo.append(arr[i])

    return golo 

            