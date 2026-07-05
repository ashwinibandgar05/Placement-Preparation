def find_duplicate(nums):
    hashmap={}
    output=[]
    for i in nums:
        if i in hashmap:    #here i is an element in hashmap not the index
            hashmap[i]+=1

        else:
            hashmap[i]=1

    for i in hashmap:
        if hashmap[i]>=2:
            output.append(i)

    return output

print(find_duplicate([1,2,3,2,3,4,2,5,4,5]))
