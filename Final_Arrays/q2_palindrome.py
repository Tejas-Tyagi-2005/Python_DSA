# Check if a string is a palindrome (same forward and backward).
# Return True or False.


def string_rev(s):

        result = ""
    
        for i in range(len(s)-1 , -1 ,-1):
         result += s[i]

        return result





def palindrome_check(s):
    
    if string_rev(s) == s:
         return True  
    else :
         return False
        

print(palindrome_check("RACECAR"))



