# Return True if array is sorted in non-decreasing order, else False.

def sort_checker(arr):

    sorted = False

    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return  False 
    return True



print(sort_checker([1,2,3,4,5,6,9,67]))
   