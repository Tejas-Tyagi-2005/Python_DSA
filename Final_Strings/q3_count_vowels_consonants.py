# Count number of vowels and consonants in a string.
# Return both counts.

def vowel_count(s):
    s = s.lower()

    vowel_count = 0

    cons_count = 0 


    vowels = ['a','e','i','o','u']


    for i in range(len(s)): # range already gives on -1 less than the actual lenght 
        if s[i] in vowels:
            vowel_count += 1
        else :
            cons_count += 1

    return vowel_count , cons_count 
               

print(vowel_count("Tejas"))