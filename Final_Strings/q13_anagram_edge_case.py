# Check if two strings are anagrams ignoring spaces and case.
# Return True or False.

def rm(s):

    result = ""

    for char in s:
        if char != " ":
            result += char 
    return result 


def ana(s,d):


    s = s.lower()
    d = d.lower()
    s = rm(s)
    d = rm(d)

    if sorted(s) == sorted(d):
        return True 
    
    else:
        return False
    
print(ana("h j E","e  J p"))    


