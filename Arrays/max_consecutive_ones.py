# Return the maximum number of consecutive 1s in the list.
# Example: [1,1,0,1,1,1] → 3

def max_consec(arr):

    current  = 0

    max_count = 0  

    for i in range(len(arr)):
        if arr[i] == 1 :
            current += 1
        else: 
            current = 0 

        if max_count < current:
            max_count = current

    return max_count  


print(max_consec([1,2,3,4,5,1,1,1]))
       

