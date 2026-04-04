# Find the maximum element in a list of numbers.
# Return the maximum value.

def max_element(arr):

    max_val = arr[0]

    for i in range(len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]

    return max_val        

print(max_element([1,2,3,4,5,9,8,3,56]))