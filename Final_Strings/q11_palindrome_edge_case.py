# Check if a string is a palindrome ignoring spaces and case.
# Return True or False.


def rm(s):

    result = ""

    for char in s:
        if char != " ":
            result += char
    return result 
        

def pal(s):

    
    s= rm(s)
    s= s.lower()

    left = 0 

    right = len(s)-1

    while left < right:
        if s[left] != s[right]:
            return False
        
        left += 1
        right -= 1

    return True 


print(pal("n I t in"))

    



