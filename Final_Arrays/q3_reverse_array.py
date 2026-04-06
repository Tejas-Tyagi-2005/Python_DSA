# Reverse the given array in-place.
# Return the array.

def rev(arr):

    result = []

    for i in range(len(arr)-1 , -1 , -1):
        result.append(arr[i])
    return result 

print(rev([1,2,3,4,5,6,7,8,9,10]))       