#Given an array, find:

# The sum of the second-largest element and the smallest element.


def largeSmall(arr):

    largest = arr[0]


    smallest = arr[0]

    second_largest = None 


    for i in range(1,len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]

        
        elif arr[i] != largest and (second_largest is None or  arr[i] > second_largest):
            second_largest = arr[i]


        if arr[i] < smallest:
            smallest = arr[i]

        
    val = smallest + second_largest
    return val 




                     