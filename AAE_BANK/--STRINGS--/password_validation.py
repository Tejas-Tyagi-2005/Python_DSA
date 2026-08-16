# password valition 


def pasa(password):

    is_upper = False
    is_lower = False
    is_digit = False 
    is_speacial = False 

    if len(password) < 8:
        return "Invalid"

    for char in password:

        if char.isupper():
            is_upper = True 

        elif char.islower():
            is_lower = True 

        elif char.isdigit():
            is_digit = True

        elif not char.isalnum():
            is_speacial = True 

    if is_upper and is_lower and is_digit and is_speacial:
        return "Valid"     
    return "Invalid"
                           