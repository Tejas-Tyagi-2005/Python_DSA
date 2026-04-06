# Find the maximum and minimum element in an array.
# Return both values.

def max_val(arr):

    max_val = arr[0]

    min_val = arr[0]

    for i in range(len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    


    for i in range(len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
    return min_val,max_val


print(max_val([1,2,3,4,5,6,8]))