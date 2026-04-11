# Return list of averages of every window of size k.

def avg_arr(arr,k):
    result = []
    
    window_sum = sum(arr[:k])
    
    result.append(window_sum / k)
    
    for i in range(k,len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        result.append(window_sum / k)
        
        
        
    return  result 
    

print(avg_arr([1,2,3,4,56,78,9,87,6,5,43,2,1],3))    
    