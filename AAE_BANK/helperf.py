# ============================================================
# TASK
# ============================================================
#
# Create a helper function that returns a new list containing
# ONLY the positive numbers from arr.
#
# Then use that helper to solve the previous problem:
#
#     second-largest DISTINCT + smallest
#



def helper(arr):

    correct_arr = []


    for i in arr:
        if i > 0 :
            correct_arr.append(i)

    return correct_arr      


def var(arr):

    arr = helper(arr)


    largest = arr[0]

    second_largest = None 

    Smallest = arr[0]


    for i in range(1,len(arr)):

        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]

        elif arr[i] != largest and (second_largest is None or arr[i] > second_largest):
            second_largest = arr[i]

        if arr[i] < Smallest:
            Smallest = arr[i]

    val = Smallest +second_largest


    return val



