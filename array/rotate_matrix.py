def rotate_image(matrix):
    for i in range(len(matrix)):
        for j in range(i,len(matrix[i])):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

    for i in range(len(matrix)):
        matrix[i].reverse()


    return matrix

print(rotate_image([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))