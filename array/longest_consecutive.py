def longest_consecutive(nums):
    num_set=set(nums)
    longest=0
    arr=[]
    
    
    for num in num_set:
        if num-1 not in num_set:
            current=num
            length=1
            

            while current+1 in num_set:
                arr.append(current)
                current+=1
                length+=1
            
            longest=max(longest,length)

    return longest ,arr




print(longest_consecutive([1,8,35,29,5,7,2,4,3,6]))