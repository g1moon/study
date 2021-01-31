# boj 

m,n = map(int,input().split())
mat = [list(input()) for _ in range(m)]
ans_mat1 = [list('WBWBWBWB') if i % 2 == 0 else list('BWBWBWBW') for i in range(8)]
ans_mat2 = [list('BWBWBWBW') if i % 2 == 0 else list('WBWBWBWB') for i in range(8)]

for start_x in range(m-7):
    for start_y in range(n-7):
        #--------------------------------
        res1 = 0
        for i in range(8):
            for j in range(8):
                nx = start_x + i
                ny = start_y + j
                if mat[nx][ny] != ans_mat1[i][j]:
                    res1 += 1
        #---------------------------------------
        res2 = 0            
        for i in range(8):
            for j in range(8):
                nx = start_x + i
                ny = start_y + j
                if mat[nx][ny] != ans_mat2[i][j]:
                    res2 += 1
        #----------------------------------
        
print(min(res1, res2))
                    
        
        