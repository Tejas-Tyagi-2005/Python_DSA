# Find the first character in a string that does not repeat.
# Return the character (or None if all repeat).

def non_repeater(s):
    s = s.lower()
    char = ''

    repeater_list = {}
    # filling up the repeater_list with all the elements
    for char in s:
        if char in repeater_list:
            repeater_list[char] += 1
        else:
            repeater_list[char] = 1


    for char in s:
        if repeater_list[char] == 1:
         return char
       
           
    return None
        

print(non_repeater("Oeousphagus"))