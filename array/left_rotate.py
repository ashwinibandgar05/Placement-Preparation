def left_rotate_array(arr):
    temp=arr[0]
    for i in range(len(arr)-1):
        arr[i]=arr[i+1]

    arr[-1]=temp

    return arr

print(left_rotate_array([1,2,3,4,5]))