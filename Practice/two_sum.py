# Q7: Two Sum
# Given an array nums and an integer target,
# return indices of the two numbers such that they add up to target
# You may assume exactly one solution exists
# You may not use the same element twice
# Return answer in any order
# Example: nums = [2,7,11,15], target = 9 -> [0,1]
# Example: nums = [3,2,4], target = 6 -> [1,2]


def two_sum(nums,target):

    seen = {}
   

    for i in range(len(nums)):
       needed = target - nums[i]

       if needed in seen:
           return seen[needed] , i 


       seen[nums[i]] = i

print(two_sum([1,2,3,4,5,6],3))
