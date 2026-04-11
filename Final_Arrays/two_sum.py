# Given a sorted array and target,
# return True if any pair adds to target.

def two_sum(arr,target):
    
    left = 0 
    right = len(arr) -1 
    
    while left < right:
        
        current = arr[left] + arr[right]
        
        if current == target:
            return True 
        elif current < target:
            left += 1
        elif current > target:
            right -= 1
            
    
    return False
    
print(two_sum([1,2,3,4,5,6,7,8,9],65784))    