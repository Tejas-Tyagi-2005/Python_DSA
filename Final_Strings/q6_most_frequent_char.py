# Find the character with the highest frequency in a string.
# Return the character.

def highest_freq(s):

    max_char = ''
    max_count = 0 

    freq = {}

    for char in s:
        if char in freq:
            freq[char] += 1
        else :
            freq[char] = 1


    for char in freq:
        if freq[char] > max_count:
            max_count = freq[char]
            max_char = char 

    return max_char












    