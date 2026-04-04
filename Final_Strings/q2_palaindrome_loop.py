# Check if a string is a palindrome (same forward and backward).
# Return True or False. Using loops



def palindrome_check(s):

    left = 0

    right = len(s)-1

    while left < right:
        if s[left] != s[right]:
            return False
        
        left += 1 
        right = right - 1    
            

    return True    
      
               
print(palindrome_check("NITIN"))               

