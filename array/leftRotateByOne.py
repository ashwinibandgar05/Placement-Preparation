def left_rotate(nums):
    first=nums[0]
    for i in range(len(nums)-1):
        nums[i]=nums[i+1]

    nums[-1]=first

    return nums

print(left_rotate([1,2,3,4,5]))