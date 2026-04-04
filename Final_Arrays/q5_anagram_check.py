# Check if two strings are anagrams (same characters, same frequency).
# Return True or False.

def string_anagrams(s,s1):
    if len(s) != len(s1):
        return False
    
    s = s.lower()
    s1 = s1.lower()

    if sorted(s) == sorted(s1):
        return True
    else :
        return False
    
print(string_anagrams("Gobi" , "Boge"))    