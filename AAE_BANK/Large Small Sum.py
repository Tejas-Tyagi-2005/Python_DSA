#Given an array, find:

# The sum of the second-largest element and the smallest element.


def helper(arr):

    largest = arr[0]

    second_largest = 0

    for i in range(len(arr)):
        if arr[i] > largest and arr[i] > second_largest:
            second_largest = largest
            largest = arr[i]
    return second_largest

def largeSmall(arr):

    second_largest  = helper(arr)

    smallest = arr[0]

    for i in arr:
        if i < smallest:
            smallest = i

    return smallest + second_largest








