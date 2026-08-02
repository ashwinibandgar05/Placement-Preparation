def largestNiceSubstring(s):
    ans=""
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            sub=s[i:j]
            if isNice(sub):
                if len(ans)<len(sub):
                    ans=sub
    return ans

def isNice(sub):
    st=set(sub)

    for ch in st:
        if ch.lower() not in st or ch.upper() not in st:
            return False
    return True


print(largestNiceSubstring("YazaAay"))
print(largestNiceSubstring("Bb"))
print(largestNiceSubstring("c"))