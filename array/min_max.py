def min_max(nums):
    maximum=0
    minimum=nums[0]
    for i in nums:
        if i>maximum:
            maximum=i
        elif i<minimum:
            minimum=i

    return minimum,maximum

print(min_max([42,98,56,36,47,19,48]))