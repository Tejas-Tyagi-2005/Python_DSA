# Remove all occurrences of x from the list in-place.
# Return the new length (elements before that index are valid).

def remove(arr,x):
    j = 0 

    for i in range(len(arr)):
        if arr[i] != x :
            arr[j] = arr[i]
            j+=1
    return j 


print(remove([1,2,3,4,5,6,7],4))
