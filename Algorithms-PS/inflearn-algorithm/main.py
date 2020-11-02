'''
- N개의 도시 
'''

#input()
N, M = map(int, input().split())
mat = [ [10000] * N for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    mat[a-1][b-1] = c

#자기자신 = 0 -------------------
for i in range(N):
    mat[i][i] = 0
#-------------------------------

#프롤이드워샬----------------------------------
'''
-k는 0일때-> 00 000 // 01 001 // 02 002 
        -> 10 100 // 11 101 // 12 102 
        -> 20 200 // 21 201 // 22 202 
        
-k는 1일떄-> 00 010 // 01 011 // 02 012
...
이런식으로 모든 거 다 고려 해서 업뎃
'''
for k in range(N): #0부터 n-1까지
    for i in range(N):
        for j in range(N):
            mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])
#---------------------------------------------
#출력
for i in mat:
    print(i)
 

