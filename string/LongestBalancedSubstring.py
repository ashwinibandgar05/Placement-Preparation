"""2609. Find the Longest Balanced Substring of a Binary String
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are given a binary string s consisting only of zeroes and ones.

A substring of s is considered balanced if all zeroes are before ones and the number of zeroes is equal to the number of ones inside the substring. Notice that the empty substring is considered a balanced substring.

Return the length of the longest balanced substring of s.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "01000111"
Output: 6
Explanation: The longest balanced substring is "000111", which has length 6.
Example 2:

Input: s = "00111"
Output: 4
Explanation: The longest balanced substring is "0011", which has length 4. 
Example 3:

Input: s = "111"
Output: 0
Explanation: There is no balanced substring except the empty substring, so the answer is 0."""



def LongestSubstringBalanced(s):
    ans=0
    zeros=0
    ones=0
    for i in range(len(s)):
        if s[i]=='0':
            if i>0 and s[i-1]=='1':
                zeros=0
                ones=0
            zeros+=1
        else:
            ones+=1
            ans=max(ans,2*min(zeros,ones))

    return ans

print(LongestSubstringBalanced("010101"))
print(LongestSubstringBalanced("00110011"))
print(LongestSubstringBalanced("000111000"))
print(LongestSubstringBalanced("111"))