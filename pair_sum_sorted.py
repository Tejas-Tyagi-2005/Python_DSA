# Given a SORTED array and a target,
# return True if any two numbers sum to target, else False.

def pair_sum(arr,target):

    j = 0 

    i = 1 

    for i in range(len(arr)-1):
        if arr[j] + arr[i] == target:
            return True 
        else :
            j += 1 
            i += 1 
            
      