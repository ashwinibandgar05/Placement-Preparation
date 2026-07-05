def merge_sorted_array(arr1,arr2):
    output=[]
    
    
    i=0
    j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            output.append(arr1[i])
            i+=1

        else :
            output.append(arr2[j])
            j+=1

    while i<len(arr1):
        output.append(arr1[i])
        i+=1

    while j<len(arr2):
        output.append(arr2[j])
        j+=1

        


    return output


print(merge_sorted_array([1,3,5],[1,2,4,6,7]))