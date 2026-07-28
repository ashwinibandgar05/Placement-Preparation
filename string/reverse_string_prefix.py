"""3794. Reverse String Prefix
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are given a string s and an integer k.

Reverse the first k characters of s and return the resulting string.

 

Example 1:

Input: s = "abcd", k = 2

Output: "bacd"

Explanation:​​​​​​​

The first k = 2 characters "ab" are reversed to "ba". The final resulting string is "bacd".

Example 2:

Input: s = "xyz", k = 3

Output: "zyx"

Explanation:

The first k = 3 characters "xyz" are reversed to "zyx". The final resulting string is "zyx".

Example 3:

Input: s = "hey", k = 1

Output: "hey"

Explanation:

The first k = 1 character "h" remains unchanged on reversal. The final resulting string is "hey".

 """


def reverse(s,k):
    s=list(s)

    for i in range(len(s)):
        if i==k-1:
            s[0:i+1]=reversed(s[0:i+1])

    return "".join(s)



print(reverse("xyz",3))

print(reverse("abcd",2))

print(reverse("hey",1))