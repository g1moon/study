import sys
sys.setrecursionlimit(100000)
n,m = map(int, sys.stdin.readline().split())
mat = [[0] * (m+1)]
for _ in range(n):
    row =[0] +  list(map(int, input().split()))
    mat.append(row)
    
for x in range(1, n+1):
    for y in range(1, m+1):
        mat[x][y] = mat[x][y] + max(mat[x-1][y], mat[x-1][y-1], mat[x][y-1])
print(mat[n][m])
    



