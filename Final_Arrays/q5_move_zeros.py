# Move all zeros in the array to the end while maintaining order of non-zero elements.
# Return the modified array.

def move_zero(arr):

    j = 0 

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j] = arr[i]
            j += 1

    for i in range(j, len(arr)):
        arr[i] = 0

    return  arr    

print(move_zero([1,2,3,40,0,2,3,0,2]))