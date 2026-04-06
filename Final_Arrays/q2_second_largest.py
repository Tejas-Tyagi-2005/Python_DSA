# Find the second largest element in an array.
# Return the value.

def sec_lar(arr):

    largest = float("-inf")

    second_largest = float("-inf")

    for i in arr:
        if i > largest:
            second_largest = largest
            largest = i 
        elif i < largest and i > second_largest:
            second_largest = i
    return second_largest

print(sec_lar([3,3,3,3,3,3,3,3]))            
