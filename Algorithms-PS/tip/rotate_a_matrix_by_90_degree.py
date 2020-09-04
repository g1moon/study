
def rotate_a_matrix_by_90_degree(mat):
    row_len = len(mat) #행길이
    col_len = len(mat[0]) #열길이
    res = [[0] * row_len for _ in range(col_len)] #결과리스트
    for i in range(row_len):
        for j in range(col_len):
            res[j][row_len-i-1] = mat[i][j]
    return res


mat = [[0,1,0], [0,0,0],[0,1,1]]
print('-----org--------')
for i in range(len(mat)):
    print(mat[i])
print('------rotate_a_matrix_by_90_degree-----------')
mat1 = rotate_a_matrix_by_90_degree(mat)
for i in range(len(mat)):
    print(mat1[i])
print('------np.rot90()-------------')
import numpy as np
print(np.rot90(mat))
