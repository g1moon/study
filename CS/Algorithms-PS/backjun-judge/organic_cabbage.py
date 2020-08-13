import sys
sys.setrecursionlimit(10000)

T = int(input())
B, ck = [] , []

dx, dy = [1,0,-1,0], [0,1,0,-1]

def dfs(x,y):
    global B, ck 
    #이미 들른 곳이 아니라면
    if ck[x][y] == 1:
        return 
    #ck를 1로 바꿔주고
    ck[x][y] = 1
    #동서남북살핌
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        #만약 동서남북 0이거나 이미 확인 된 곳이라면 
        if B[xx][yy] == 0 or ck[xx][yy] == 1:
            continue
        #아니라면 이 곳을 본다
        dfs(xx,yy)
        

def process():
    
    global B,ck 
    M,N,K = map(int, input().split())
    
    B = [[0 for i in range(50 + 2)] for _ in range(50+2)]
    ck = [[0 for i in range(50 + 2)] for _ in range(50+2)]
    
    for _ in range(K):
        X,Y = map(int, input().split())
        B[Y+1][X+1] = 1
        
    #####main##########################    
    ans = 0
    #추가해줫으니까 1부터 돌고 대신 +1만큼 더봐 
    for i in range(1, N+1):
        for j in range(1, M+1):
            #0이면 무시 , ck되어있으면 무시 
            if B[i][j] == 0 or ck[i][j] == 1:
                continue
            #아니면 dfs돌려 그럼 동서남북 다 볼 거야 볼거 없어지면 끝나고 그럼 1증가
            dfs(i,j)
            ans += 1
    print(ans)
    
for _ in range(T):
    process()