"""Subarray Sum Equals K
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 """


def subarray(nums,k):
    prefixSum=0
    prefixMap={0:1}
    Count=0

    for i in nums:
        prefixSum+=i
        if prefixSum-k in prefixMap:
            Count+=prefixMap[prefixSum-k]

        prefixMap[prefixSum]=prefixMap.get(prefixSum, 0) + 1
    return Count

print(subarray([1,1,1],2))