def max_sum_subarray(nums):
    max_sum=nums[0]
    curr_sum=0
    for i in nums:
        
        curr_sum=max(i,curr_sum+i)
        max_sum=max(max_sum,curr_sum)
    return max_sum

print(max_sum_subarray([2,3,6,-1,6,-4]))