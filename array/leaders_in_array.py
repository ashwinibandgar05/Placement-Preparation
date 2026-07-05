def leader(nums):
    answer=[]
    n=len(nums)
    max_right=nums[-1]
    answer.append(max_right)
    for i in range(n-2,-1,-1):
        if nums[i]>max_right:
            answer.append(nums[i])
            max_right=nums[i]

    answer.reverse()
    return answer

print(leader([17,17,4,3,5,2]))
