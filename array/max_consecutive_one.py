# Given a binary array nums, return the maximum number of consecutive 1s in the array.
# A binary array is an array that contains only 0s and 1s.


def max_cons_one(nums):
    count=0
    for i in range(len(nums)-1):
        if nums[i]==1:
            if nums[i]==nums[i+1]:
                count+=1

    return count

print(max_cons_one([1,1,0,0,1,1,1]))