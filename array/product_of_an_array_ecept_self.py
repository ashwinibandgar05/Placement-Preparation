# Problem Statement
# Given an integer array nums, return an array answer such that:
# answer[i] = product of all elements of nums except nums[i]

def product(arr):
    n=len(arr)
    answer=[1]*n

    left_product=1

    for i in range(n):
        answer[i]=left_product
        left_product*=arr[i]


    right_product=1
    for i in range(n-1,-1,-1):
        answer[i]*=right_product
        right_product*=arr[i]

    return answer

print(product([1,2,3,4]))