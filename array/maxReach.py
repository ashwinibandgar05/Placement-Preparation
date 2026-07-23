def canReach(nums):
    maxReach=0

    for i in range(len(nums)):
        if i>maxReach:
            return False


        maxReach=max(maxReach,i+nums[i])

    return True



print(canReach([3,2,1,0,4]))