def prefix(strs):
    prefix=strs[0]

    for i in range(len(prefix)):
        ch=prefix[i]

        for word in strs:
            if i>=len(word) or word[i]!=ch:
                return prefix[:i]

    return prefix



print(prefix(["flower","flow","flight"]))

print(prefix(["dog","racecar","car"]))
