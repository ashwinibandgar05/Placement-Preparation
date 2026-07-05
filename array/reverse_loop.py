def reverse(nums):
    n=len(nums)
    output=[]
    for i in range(n-1,-1,-1):
        output.append(nums[i])

    return output

print(reverse([1,2,3,4,5]))