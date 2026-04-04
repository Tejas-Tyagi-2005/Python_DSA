# Remove all spaces from a string.
# Return the modified string.

def space_remove(s):

    modified_string = ""

    for char in s:
        if char != " ": # " " used to denote empty space , not ('-inf)
            modified_string += char # += used for strings , .add() used for sets 

    return modified_string

print(space_remove("Tejas  Tyagi "))

