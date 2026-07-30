"""415. Add Strings
Solved
Easy
Topics
premium lock icon
Companies
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output:0"""


def Addition(num1,num2):

    i=len(num1)-1
    j=len(num2)-1
    carry=0
    ans=[]
    while i>=0 or j>=0 or carry:
        digit1=ord(num1[i])-ord('0') if i>=0 else 0
        digit2=ord(num2[j])-ord('0') if j>=0 else 0

        total=digit1+digit2+carry

        ans.append(str(total%10))
        carry=total//10

        i-=1
        j-=1

    return "".join(ans[::-1])


print(Addition("11","123"))


print(Addition("456","77"))