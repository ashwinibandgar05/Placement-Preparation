def majority(nums):
    majority_element={}
    for i in nums:
        if i not in majority_element:
            majority_element[i]=1
        else:
            majority_element[i]+=1

    return max(majority_element,key=majority_element.get)


print(majority([2,2,2,1,1,4,1,1]))