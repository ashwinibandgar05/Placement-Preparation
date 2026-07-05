def missing_no(arr):
    n=len(arr)+1
    required_sum=n*(n+1)//2
    actual_sum=sum(arr)
    return required_sum-actual_sum


print(missing_no([1,2,3,4,5,7,8]))