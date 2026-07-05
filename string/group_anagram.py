def group_anagram(s):
    hashmap={}

    for i in s:
        
        sort_i="".join(sorted(i))  #sorted(i)gives the seperate character so must make it string
       
        if sort_i in hashmap:
            hashmap[sort_i].append(i)
        
        else:
            hashmap[sort_i]=[i]
        
    return list(hashmap.values())


print(group_anagram(["eat","tea","tan","ate","nat","bat"]))


