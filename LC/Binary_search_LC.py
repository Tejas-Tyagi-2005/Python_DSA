# Q4: Binary Search
# nums is sorted in ascending order
# Return index of target if found
# If target does not exist, return -1
# Example: nums = [-1,0,3,5,9,12], target = 9 -> 4
# Example: nums = [-1,0,3,5,9,12], target = 2 -> -1


def Binary(nums,target):

    left = 0 
    right = len(nums)-1
    
    for i in range(len(nums)):
        mid = (left + right)//2

        if nums[mid] == target:
            return mid
        
        elif nums[mid] > target:
            right = mid -1 
            
        elif nums[mid] < target:
            left = mid + 1
            
            
    return -1 

print(Binary([1,2,3,4,5,6,7,8,9],8))
