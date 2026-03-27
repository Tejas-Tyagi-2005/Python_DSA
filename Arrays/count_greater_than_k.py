# Return how many elements in the list are greater than k.
# Use a loop.

arr = list(map(int,input("Enter the elements of the array :").split()))

k = int(input("Enter the value of k "))

count = 0 

for i in arr:
    if i > k :
        count += 1 


print(count)
