def remove_duplicates(nums):
    output=[]
    for i in nums:
        if i not in output:
            output.append(i)
    return output


print(remove_duplicates([1,4,2,2,3,5,6,7,3,1,8,4]))