"""49. Group Anagrams
Solved
Medium
Topics
premium lock icon
Companies
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 """


def group_anagram(s):
    hashmap={}

    for i in s:
        
        sort_i="".join(sorted(i))  #sorted(i)gives the seperate character so must make it string
       
        if sort_i in hashmap:
            hashmap[sort_i].append(i)
        
        else:
            hashmap[sort_i]=[i]
        
    return list(hashmap.values())


print(group_anagram(["eat","tea","tan","ate","nat","bat"]))


# Other answers is 
"""
class Solution(object):
    def groupAnagrams(self, strs):
        
        hashmap={}
        for s in strs:
            key="".join(sorted(s))
            if key not in hashmap:
                hashmap[key]=[]
            hashmap[key].append(s)

        return list(hashmap.values())
        
"""