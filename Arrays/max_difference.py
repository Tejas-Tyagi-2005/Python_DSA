# Return the difference between max and min element in the list.


def max_diff(arr):
    max_val = arr[0]
    min_val = arr[0]

    for i in arr:
        if max_val < i:
            max_val = i
        if min_val > i:
            min_val = i

    return max_val - min_val

print(max_diff([1,2,3,4,5,6]))           



    
 
