"""1624. Largest Substring Between Two Equal Characters
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.
Example 2:

Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".
Example 3:

Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.
 """

def max_len_bet_two_same_char(s):
    ans=-1
    s=list(s)
    for i in range(len(s)):
        for j in range(len(s)-1,i,-1):
            if s[i]==s[j]:
                ans=max(ans,j-i-1)
                break
    return ans

print(max_len_bet_two_same_char("aa"))
print(max_len_bet_two_same_char("abca"))
print(max_len_bet_two_same_char("cbzxy"))
