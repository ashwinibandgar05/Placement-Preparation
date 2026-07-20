def set_zeros(matrix):

    m=len(matrix)
    n=len(matrix[0])

    row=[False]*m
    col=[False]*n

    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                row[i]=True
                col[j]=True

    for i in range(m):
        for j in range(n):
            if row[i] or col[j]:
                matrix[i][j]=0

    return matrix


print(set_zeros([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))