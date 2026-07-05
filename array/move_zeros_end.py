def move_zero(nums):
    pos=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[pos],nums[i]=nums[i],nums[pos]
            pos+=1

    return nums


    

print(move_zero([1,0,3,0,4,0,2,0,5]))