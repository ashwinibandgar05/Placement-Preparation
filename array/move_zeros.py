def moveZero(nums):
    j=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            j+=1

    return nums


print(moveZero([0,0,2,5,0,10,9,0,4,2,0,6,5,0,0,0,2]))