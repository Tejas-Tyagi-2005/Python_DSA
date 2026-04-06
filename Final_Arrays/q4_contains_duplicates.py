# Check if an array contains any duplicate elements.
# Return True if duplicates exist, otherwise False.


def duplicate(arr):

    seen = set()

    for i in arr:
        if i in seen:
            return True 
        seen.add(i)
    return False     


       

