def is_palindrome(num):
    reverse=0
    original=num
    while num>0:
        digit=num%10
        reverse=reverse*10+digit
        num//=10

    return reverse==original

print(is_palindrome(12321))