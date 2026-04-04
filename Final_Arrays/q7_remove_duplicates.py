# Remove duplicate characters from a string.
# Return the string with only first occurrences (preserve order).

def duplicate_remover(s):
    s = s.lower()
    seen = set()
    result = ""

    for char in s:
        if char not in seen:
            result += char 
            seen.add(char)

    return result 

print(duplicate_remover("America"))        