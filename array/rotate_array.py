# def rotateArray(nums,k):
#     k=k%len(nums)
#     nums[:]=nums[-k:]+nums[:-k]
#     return nums


# print(rotateArray([1,2,3,4,5,6,7],4))



# Another approach
def rotateArray(nums,k):
    
    n=len(nums)
    k=k%n
    ans=[0]*n
    for i in range(n):
        ans[(i+k)%n]=nums[i]

    for i in range(n):
        nums[i]=ans[i]

    return nums

print(rotateArray([1,2,3,4,5,6,7],4))


