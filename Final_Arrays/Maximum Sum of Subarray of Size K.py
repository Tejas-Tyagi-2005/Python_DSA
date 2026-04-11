# Return the maximum sum of a subarray of size k 

def max_sub(arr,k):

    window_sum = sum(arr[:k])

    maxi = window_sum

    for i in range(k,len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]

        if window_sum > maxi:
          maxi = window_sum

    return maxi

print(max_sub([1,2,3,4,5,6,7,8,9,7,6,5,4,3,56,7,89,8,76,5,4,3],1))        
