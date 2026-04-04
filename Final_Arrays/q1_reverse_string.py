# Reverse a given string without using built-in reverse functions.
# Return the reversed string.

def string_rev(s):

    result = ""
    
    for i in range(len(str)-1 , -1 , -1):
         result += str[i]

    return result
         


print(string_rev('abc'))

'''
here we start the loop from the opposite end , and use -1 to tell it we are going back 
just append the new char to the new string
print new string

'''