# Check if a string contains only digits.
# Return True or False.

def check_digit(s):

    for char in s:
        if  not char.isdigit():
            return False
        
    return True 

print(check_digit("983hi729"))    