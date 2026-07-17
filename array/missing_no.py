def missing_no(arr):
    arr.sort()
    
    
    for i in range(len(arr)-1):
        if arr[i+1]!=arr[i]+1:
            return arr[i]+1
        
    return len(arr)




print(missing_no([1,2,3,4,5,6,7,8]))