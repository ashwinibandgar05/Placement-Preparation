def two_sum(nums,target):
    hashmap={}
    for i ,num in enumerate(nums):
        complement=target-num

        if complement in hashmap:
            return [hashmap[complement],i]
        
        hashmap[num]=i



print( two_sum([2,6,4,1,5,8],6))