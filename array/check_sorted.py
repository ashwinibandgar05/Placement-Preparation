def isSorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:

            return False
        
        
    return True
        

print(isSorted([1,2,7,4,5,6]))
