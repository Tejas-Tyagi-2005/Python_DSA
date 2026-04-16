# Q3: Majority Element
# Return the element that appears more than floor(n/2) times
# Majority element is guaranteed to exist
# Example: [3,2,3] -> 3
# Example: [2,2,1,1,1,2,2] -> 2


def majority(nums):

    seen = {}

    n = len(nums)

    for i in nums:
        if i not in seen:
            seen[i] = 1
        else:
            seen[i] += 1


    for i in seen:
        if seen[i] > n//2:
           return i 
        

print(majority([2,2,1,1,1,2,2]))