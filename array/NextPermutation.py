def next_permutation(nums):
    n=len(nums)
    pivot=-1
    for i in range(n-2,-1,-1):
        if nums[i]<nums[i+1]:
            pivot=i
            break

    if pivot==-1:
        nums.reverse()
        return
    
    for i in range(n-1,pivot,-1):
        if nums[i]>nums[pivot]:
            nums[i],nums[pivot]=nums[pivot],nums[i]
            break

    right=n-1
    left=pivot+1

    while left<right:
        nums[right],nums[left]=nums[left],nums[right]
        right-=1
        left+=1

    return nums

print(next_permutation([1,2,3]))
