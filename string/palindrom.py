def isPalindrom(s):
    temp=""
    for ch in s:
        if ch.isalnum():
            temp+=ch.lower()

    right=len(temp)-1
    left=0
    while left<=right:
        if temp[left]!=temp[right]:
            return False
        left+=1
        right-=1

    return True


print(isPalindrom("A man, a plan, a canal: Panama"))


print(isPalindrom("race a car"))
