#Mooyo Mooyo
#https://www.acmicpc.net/problem/16768
def new_array(N):
    return [[False for i in range(10)] for _ in range(N)]

N,K = map(int, input().split())
M = [list(input()) for i in range(N)]
ck = new_array(N)
ck2 = new_array(N)

dx, dy = [0,1,0,-1], [1,0,-1,0]

def dfs(x,y):
    ck[x][y] = True
    ret = 1
    for i in range(4):
        xx, yy = x + dx[i], y+ dy[i]
        if xx < 0 or xx >= N or yy < 0 or yy >= 10:
            continue
        
        if ck[xx][yy] or M[x][y] != M[xx][yy]:
            continue
        ret += dfs(xx, yy)
    return ret

def dfs2(x,y,val):
    ck[x][y] = True
    M[x][y] = '0'
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if xx < 0 or xx >= N or yy < 0 or yy >=10:
            continue
        if ck2[xx][yy] or M[xx][yy] != val:
            continue 
        dfs2(xx,yy, val)

#my down code 
def down(M):
    for c in range(10):
        tmp = []
        for r in range(N):
            if M[r][c] != '0':
                tmp.append(M[r][c])
        
        for rr in range(N):
            if rr >= (N- len(tmp)):
                M[rr][c] = tmp.pop(0)
            else:
                M[rr][c] = '0'
                

# def down():
#     for i in range(10):
#         tmp = []
#         for j in range(N):
#             if M[j][i] != '0':
#                 tmp.append(M[j][i])
        
#         for j in range(N-len(tmp)):
#             M[j][i] = '0'
        
#         for j in range(N-len(tmp), N):
#             M[j][i] = tmp[j - (N-len(tmp))]


while True:
    exist = False
    ck = new_array(N)
    ck2 = new_array(N)
    
    for i in range(N):
        for j in range(10):
            if M[i][j] == '0' or ck[i][j]:
                continue
            
            res = dfs(i,j)
            if res >= K:
                dfs2(i, j, M[i][j])
                exist = 
    #다봤는데도 지워질게 없으면 종료 
    if not exist:
        break
    down(M)
    
for i in M:
    print(''.join(i))