# Remove duplicate characters from a string.
# Return the string with only first occurrences (preserve order).

def duplicate_remover(s):
    s = s.lower()
    seen = set() # collection of elements already seen
    result = "" # building the new string ,only adding unique elements

    for char in s:
        if char not in seen: # if char is not in seen set 
            result += char 
            seen.add(char) # add it in seen set  , so it is not added again 

    return result 

print(duplicate_remover("America"))        