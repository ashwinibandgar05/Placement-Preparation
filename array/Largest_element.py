def largest_element(nums):
    largest=nums[0]
    for i in range(1,len(nums)):
        if nums[i]>largest:
            largest=nums[i]

    return largest

print(largest_element([4,29,48,14,97,26,17]))