# Print all pairs (i, j) where i < j.
# Example: [1,2,3] → (1,2), (1,3), (2,3)

def print_pair(arr):

    j = 0
    i=1

    for i in range(len(arr)-1):
        if arr[j] < arr[i]:
            print(arr[j],arr[i])

    return 