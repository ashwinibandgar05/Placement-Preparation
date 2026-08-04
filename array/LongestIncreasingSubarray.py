def longestIncreasing_subarray(arr):
    ans=1
    maxi=1
    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            ans+=1
        else:
            ans=1
        maxi=max(ans,maxi)
    return maxi

print(longestIncreasing_subarray([1,2,3,4,5,3,6,7,8,9]))
print(longestIncreasing_subarray([1,2,3,4,5,6,7,8,9,1,2,3,4,5]))
print(longestIncreasing_subarray([2,2,2,2]))