# LeetCode Problem 1: Two Sum
# EASY LEVEL


'''
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

'''

nums = [1,3,6,3,4,9,3,2,6,4,6,3,8,5,4,6,3,6,3,6,6]

target = 8

i = nums[0] # pointer 1

j = nums[1] # pointer 2

def TwoSum(nums , target, i , j ):

 for i in range(len(nums)):
   for j in range(i + 1 , len(nums)):
   
 
     if nums[i] + nums[j] == target :
      print(f" The indices are {nums[i]} and {nums[j]}")
      return 0

# test 

TwoSum(nums , target , i ,j)



