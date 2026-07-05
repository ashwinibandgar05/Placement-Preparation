def reverse_string(str):
    n=len(str)
    output=[]
    for i in range(n-1,-1,-1):
        output.append(str[i])
    
    return "".join(output)
    
print(reverse_string("abcdefg"))

