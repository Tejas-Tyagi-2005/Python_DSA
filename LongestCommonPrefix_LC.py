# Leetcode Problem 2 : Longest Common Prefix 
# EASY


'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

'''

strs = [ "Flower","Flight", "Flow"]


def longestCommonPrefix(strs):
    
    Prefix = ""

    for i in range (len(strs[0])):

        char = strs[0][i]

        for words in strs[1:]:

            if i>= len(words) or words[i] != char :   
              return Prefix
        Prefix += char

    return  Prefix

print(longestCommonPrefix(strs))    