"""152. Maximum Product Subarray
Solved
Medium
Topics
premium lock icon
Companies
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray."""


def maxProduct(nums):
    max_product=nums[0]
    min_product=nums[0]

    ans=nums[0]

    for i in nums[1:]:
        if i<0:
            max_product,min_product=min_product,max_product

        max_product=max(i,max_product*i)
        min_product=min(i,min_product*i)

        ans=max(ans,max_product)

    return ans


print(maxProduct([2,3,-2,4]))