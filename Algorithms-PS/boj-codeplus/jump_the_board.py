'''
- Jump The Board!
- (nn game board)
- goal : jump along any path from the upper left to lower right corner
- all steps must be either to the right or toward the bottom
'''
n = int(input())
mat = [list(map(int,input().split())) for _ in range(n)]
dy = [[0]*n for _ in range(n)]
dy[0][0] = 1

def pp(mat):
    for i in mat:
        print(i)
    print('-'*15)
    
for i in range(n):
    for j in range(n):
        if mat[i][j] == 0:
            continue
        if j + mat[i][j] < n:
            dy[i][j+mat[i][j]] += dy[i][j]
            pp(dy)
        if i + mat[i][j] < n:
            dy[i+mat[i][j]] [j] += dy[i][j]
            pp(dy)
print(dy[n-1][n-1])

        

# def dfs(x,y):
#     global res
    
#     #종료조건
#     if x == (n-1) and y == (n-1):
#         res += 1
#         return 
#     if mat[x][y] == 0: return
#     #조건 맞으면 dfs
#     nx, ny = (x + mat[x][y]), y

        
#     if nx >= 0 and ny >= 0 and nx < n and ny <n:
#         dfs(nx, ny)
            
#     nx, ny = x, y + mat[x][y]

    
#     if nx >= 0 and ny >= 0 and nx < n and ny <n:
#         dfs(nx, ny)


# n = int(input())
# mat = [ list(map(int, input().split())) for _ in range(n)]
# res = 0
# # print(n)
# # print(mat)
# dfs(0,0)
# print(res)