def uniqueChar(s):
    hashAns={}
    for i in range(len(s)):
        if s[i] not in hashAns:
            hashAns[s[i]]=1
        else:
            hashAns[s[i]]+=1

    for i in range(len(s)):
        if hashAns[s[i]]==1:
            return i
    return -1

print(uniqueChar("leetcode"))

print(uniqueChar("loveleetcode"))

print(uniqueChar("aabb"))