# Given a list of numbers, find and return the maximum element.

def max_num(arr):

    max_val = arr[0]

    for i in range(len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val 

print(max_num([1,2,3,4,6,6,6,329]))        