# Return the second largest element in the list.
# Assume all elements are distinct.

def sec_lar(arr):
    max_val = arr[0]

    sec_val = float('-inf')

    for i in arr:
        if i > max_val:
            sec_val = max_val
            max_val = i 
        elif i > sec_val and i < max_val:    
            sec_val = i
    return sec_val

print(sec_lar([1,2,3,4,5,9]))        


