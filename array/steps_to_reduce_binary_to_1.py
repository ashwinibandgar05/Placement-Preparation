def numSteps(s):
    step=0
    num=int(s,2) #here (s,2) represent the string is in binary fform

    while num>1:
        if num%2==0:
           num=num//2
           step+=1

        else:
            num+=1
            num=num//2
            step+=2
    return step

print(numSteps("1101"))