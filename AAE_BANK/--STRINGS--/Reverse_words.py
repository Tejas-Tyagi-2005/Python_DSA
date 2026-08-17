'''
Reverse the order of the words in a sentence 

'''

def rev(sentence):

    words = []

    current_words = ""

    for char in sentence:

        if char != "":
            current_words += char

        else:
            words.append(current_words)
            current_words = ""

    words.append(current_words)


    result = ""

    for i in range(len(words)-1,-1,-1):
        if result != "":
            result += " "
        result += words[i]
    return result                     