def min_steps(nums):
    step=0
    negative=0
    zero=0
    for num in nums:
        if num>0:
            step+=num-1
        elif num<0:
            step+=(-1-num)
            negative+=1

        else:
            step+=1
            zero+=1
    if negative%2==1 and zero==0:
        step+=2

    return step


print(min_steps([-2,4,0]))

