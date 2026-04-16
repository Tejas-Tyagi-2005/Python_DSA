# Q5: Remove Duplicates from Sorted Array
# nums is sorted in non-decreasing order
# Remove duplicates in-place so each unique element appears once
# Return number of unique elements k
# First k elements of nums should contain unique values
# Example: [1,1,2] -> k = 2, nums = [1,2,_]
# Example: [0,0,1,1,1,2,2,3,3,4] -> k = 5

def rm_dups(nums):

    j = 1
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            nums[j] = nums[i]
            j+=1
    return j         

print(rm_dups([0,0,1,1,1,2,2,3,3,4]))

