# https://www.acmicpc.net/problem/1389
# boj 1389 S1 케빈
# <메모리 : 123332, 시간 120>
'''
- 플로이드 와샬(All pairs shortest path problem)
- (start -> dest) vs (start -> intermediation -> dest)
'''
N,M = map(int, input().split())

mat = [ [float('inf')]*(N) for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    mat[a-1][b-1] = 1
    mat[b-1][a-1] = 1
    
for itm in range(len(mat)):
    for x in range(len(mat)):
        for y in range(len(mat)):
            if mat[x][y] > mat[x][itm] + mat[itm][y]:
                mat[x][y] = mat[x][itm] + mat[itm][y]
            
res_num = float('inf')
res_idx = False

for i in range(len(mat)):
    a = sum(mat[i]) - mat[i][i]
    if res_num > a:
        res_num = a
        res_idx = i+1
        
print(res_idx)
        
        
       