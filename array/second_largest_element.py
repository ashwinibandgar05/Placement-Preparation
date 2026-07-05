def second_largest(nums):
    largest=0
    second_largest=0

    for i in nums:
        if i>largest:
            second_largest=largest
            largest=i

        elif i>second_largest and i!=largest:
            second_largest=i

    return second_largest

print(second_largest([74,35,79,54,12,25,65]))

