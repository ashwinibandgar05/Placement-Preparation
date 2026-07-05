def reverse_no(n):
    reverse=0
    while n>0:
        digit=n%10
        reverse=reverse*10+digit
        n//=10

    return reverse

print(reverse_no(1234))