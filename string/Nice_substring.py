"""1763. Longest Nice Substring
Solved
Easy
Topics
premium lock icon
Companies
Hint
A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

 

Example 1:

Input: s = "YazaAay"
Output: "aAa"
Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.
Example 2:

Input: s = "Bb"
Output: "Bb"
Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.
Example 3:

Input: s = "c"
Output: ""
Explanation: There are no nice substrings.
 """


def largestNiceSubstring(s):
    ans=""
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            sub=s[i:j]
            if isNice(sub):
                if len(ans)<len(sub):
                    ans=sub
    return ans

def isNice(sub):
    st=set(sub)

    for ch in st:
        if ch.lower() not in st or ch.upper() not in st:
            return False
    return True


print(largestNiceSubstring("YazaAay"))
print(largestNiceSubstring("Bb"))
print(largestNiceSubstring("c"))