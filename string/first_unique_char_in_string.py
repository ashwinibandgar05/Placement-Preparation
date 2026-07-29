"""387. First Unique Character in a String
Solved
Easy
Topics
premium lock icon
Companies
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

Input: s = "loveleetcode"

Output: 2

Example 3:

Input: s = "aabb"

Output: -1"""


def uniqueChar(s):
    hashAns={}
    for i in range(len(s)):
        if s[i] not in hashAns:
            hashAns[s[i]]=1
        else:
            hashAns[s[i]]+=1

    for i in range(len(s)):
        if hashAns[s[i]]==1:
            return i
    return -1

print(uniqueChar("leetcode"))

print(uniqueChar("loveleetcode"))

print(uniqueChar("aabb"))