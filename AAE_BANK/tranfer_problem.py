'''
Write a function:

def first_position_sum(arr, target):

It should return the number of elements from the beginning of the array needed for their cumulative sum to reach or exceed target.

'''

def first_position_sum(arr, target):

    if arr is None:
        return -1 
    
    if not arr:
        return -1
     
    number_of_elements_before_target = 0 

    current_sum = 0 

    for i in arr:
        current_sum += i
        number_of_elements_before_target += 1

        if current_sum >= target:
            return number_of_elements_before_target

    return number_of_elements_before_target


print(first_position_sum([3, 4, 2, 8],9))

