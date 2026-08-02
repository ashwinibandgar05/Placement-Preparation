"""1446. Consecutive Characters
Solved
Easy
Topics
premium lock icon
Companies
Hint
The power of the string is the maximum length of a non-empty substring that contains only one unique character.

Given a string s, return the power of s.

 

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
 """

def maxConsString(s):
    count=1
    ans=1
    s=list(s)
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            count+=1
        else:
            count=1
        ans=max(ans,count)

    return ans

print(maxConsString("leetcode"))
print(maxConsString("abbcccddddeeeeedcba"))