# Q1: Plus One
# digits represents a number (e.g. [1,2,3] = 123)
# Add 1 to the number and return updated digits array
# Example: [1,2,3] -> [1,2,4]
# Example: [9] -> [1,0]


def PlusOne(digits):
    # Rememeber to loop from right side .
    for i in range(len(digits)-1,-1,-1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0

    return [1] + digits 

print(PlusOne([1,2,9]))
