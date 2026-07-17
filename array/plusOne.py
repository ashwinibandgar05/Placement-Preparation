def plusOne(nums):
    n=len(nums)
    for i in range(n-1,-1,-1):
        if nums[i]!=9:
            nums[i]+=1
            return nums
        
        nums[i]=0
    return [1]+nums

print(plusOne([1,2,3,4]))
