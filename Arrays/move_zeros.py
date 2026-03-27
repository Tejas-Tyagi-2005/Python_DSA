# Move all 0s to the end of the list while keeping order of non-zero elements.
# Modify and return the list.

# IMP


def move_zeros(arr):

    j = 0 

    for i in range(len(arr)):
        if arr[i] != 0 :
            arr[j] = arr[i]
            j+=1
    for i in range(j,(len(arr))):
        arr[i] = 0

    return arr

print(move_zeros([1,2,3,5,0,3,0,2,0]))            


