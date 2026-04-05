# Find the most frequent character in a string.
# Ignore spaces and treat uppercase/lowercase as same.
# Return the character.



def rm(s):

    result = ""

    for char in s:
        if char != " ":
            result += char 
    return result 


def max(s):

    freq = {}
    s = s.lower()
    s = rm(s)

    max_char = ""
    max_count = 0 

    for char in s:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1

    for char in freq:
        if freq[char] > max_count:
            max_char = char
            max_count = freq[char]

    return max_char

print(max(" lbd asiduf saisdvsbjd isubdfisf iuanOHor oI"))                    
