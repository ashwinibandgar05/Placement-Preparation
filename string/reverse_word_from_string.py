def reverseWord(s):
    words=s.split()

    for i in range(len(words)):
        words[i]=words[i][::-1]

    return " ".join(words)


print(reverseWord("Let's take LeetCode contest"))