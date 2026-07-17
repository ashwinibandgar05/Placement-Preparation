def remove_duplicates(nums):
    if not nums:
        return 0
    output=[]
    for i in range(0,len(nums)):
        if nums[i] not in output:
            output.append(nums[i])

    return output




print(remove_duplicates([0,1,4,2,2,3,5,6,7,3,1,8,4]))

