def first_non_repeating(s):
    hashmap={}
    for ch in s:
        if ch in hashmap:
            hashmap[ch]+=1
        else:
            hashmap[ch]=1

    for ch in s:
        if hashmap[ch]==1:
            return ch
        
    return -1


print(first_non_repeating("abcfdabcde"))
