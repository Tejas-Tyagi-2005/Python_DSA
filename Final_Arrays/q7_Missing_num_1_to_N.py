# Given array containing numbers from 1 to N with one missing, find the missing number.
# Return the number.

def missnum(arr):

    N = len(arr)+1

    total = 0 

    for i in range(1,N+1):
        total += i 

    actual = sum(arr)
    num = total - actual 

    return num 

print(missnum([1,2,3,4,5,6,8,9]))    