"""2485. Find the Pivot Integer
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given a positive integer n, find the pivot integer x such that:

The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input."""


def pivot_integer(n):
    total=n*(n+1)//2

    leftsum=0
    for i in range(1,n+1):
        rightsum=total-leftsum-i
        if rightsum==leftsum:
            return i
        
        leftsum+=i

    return -1


print(pivot_integer(8))