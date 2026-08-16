# ============================================================
# #9 VARIATION — ROTATE ARRAY RIGHT BY K
# ============================================================
#
# Now do the OPPOSITE of the previous problem.
#
# Rotate the array to the RIGHT by K positions.
#
# Example:
#
# arr = [1, 2, 3, 4, 5]
# k = 2
#
# Result:
#
# [4, 5, 1, 2, 3]
#
# ------------------------------------------------------------
#


def rotate(arr,k):

    golu = []

    for i in range(len(arr)-1,k+1):
        golu.append(arr[i])

    for i in range(k):
        golu.append(arr[i])

    return golu 

        

