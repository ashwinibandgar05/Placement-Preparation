def even_odd_count(nums):
    even_count=0
    odd_count=0
    for i in nums:
        if i%2==0:
            even_count+=1
        else:
            odd_count+=1

    return even_count,odd_count


print(even_odd_count([3,2,4,5,1,6,7,20,19,28,37,47]))
