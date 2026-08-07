"""3407. Substring Matching Pattern
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are given a string s and a pattern string p, where p contains exactly one '*' character.

The '*' in p can be replaced with any sequence of zero or more characters.

Return true if p can be made a substring of s, and false otherwise.

 

Example 1:

Input: s = "leetcode", p = "ee*e"

Output: true

Explanation:

By replacing the '*' with "tcod", the substring "eetcode" matches the pattern.

Example 2:

Input: s = "car", p = "c*v"

Output: false

Explanation:

There is no substring matching the pattern.

Example 3:

Input: s = "luck", p = "u*"

Output: true

Explanation:

The substrings "u", "uc", and "uck" match the pattern.

 """

class Solution(object):
    def hasMatch(self, s, p):
        left, right = p.split("*")

        start = s.find(left)

        while start != -1:
            end = start + len(left)

            if right == "" or s.find(right, end) != -1:
                return True

            start = s.find(left, start + 1)

        return False



print(Solution().hasMatch("leetcode", "ee*e"))
print(Solution().hasMatch("car", "c*v"))
print(Solution().hasMatch("luck", "u*"))