"""1957. Delete Characters to Make Fancy String
Easy
Topics
premium lock icon
Companies
Hint
A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make it fancy.

Return the final string after the deletion. It can be shown that the answer will always be unique.

 

Example 1:

Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".
Example 2:

Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".
Example 3:

Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab"."""


def delete_char_to_make_fancy(s):
    ans=[]
    for ch in s:
        if len(ans)>=2 and ans[-1]==ch and ans[-2]==ch:
            continue
        ans.append(ch)

    return "".join(ans)

print(delete_char_to_make_fancy("leeetcode"))
print(delete_char_to_make_fancy("aaabaaaa"))
print(delete_char_to_make_fancy("aab"))