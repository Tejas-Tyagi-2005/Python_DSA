# Given an array and a target, find two indices such that their values add up to the target.
# Return the indices.

def two_sum(arr , target):

    seen = {}

    for i in range(len(arr)):
        needed = target - arr[i]


        if needed in seen:
            return seen[needed] , i

        seen[arr[i]] = i 

    return None       


print(two_sum([1,2,3,4,5,67,7,7,6,5,4,3,2,1],9))
    

