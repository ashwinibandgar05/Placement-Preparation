# def isPolindrome(s):
#     n=len(s)
#     reverse=[]
#     for i in range(n-1,-1,-1):
#         reverse.append(s[i])
    
#     return "".join(reverse)==s


# print(isPolindrome("abcdcb"))


def isPolindrome(s):
    left=0
    right=len(s)-1

    while  left <right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
        
    return True

print(isPolindrome("abcdcba"))