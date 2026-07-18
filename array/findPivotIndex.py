"""724. Find Pivot Index
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1."""
def pivot(nums):
    total=sum(nums)
    leftsum=0
    for i in range(len(nums)):
        right_sum=total-leftsum-nums[i]

        if right_sum==leftsum:
            return i
        
        leftsum+=nums[i]

    return -1



print(pivot([1,7,3,6,5,6]))
