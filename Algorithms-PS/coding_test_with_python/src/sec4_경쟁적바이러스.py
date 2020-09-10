'''
- (N*N) 크기의 시험관이 있다.
- 모든 바이러스는 (1번부터 K번까지의 바이러스 종류중 하나)
- 1초마다 상하좌우 -> 증식
    - 1. 번호가 낮은 종류의 바이러스부터 증식
    - 2. 이미 다른 바이러스가 있으면 -> 그 곳에는 증식하지 않음

- (S초가 지난 후) 해당 위치에 바이러스가 존재하지 않는다면 -> 0출력
- 가장 왼쪽위는 (1,1)
- 
'''
#input---------------
N, K = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
qq = [ [] for _ in range(K+1000) ]
# print(qq)
S, qx, qy = map(int, input().split())

for i in range(N):
    for j in range(N):
        if mat[i][j] != 0:
            qq[mat[i][j]].append((i,j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
sec = 0 
while True:
    if S == 0:
        print(mat[qx-1][qy-1])
        break
    
    for i in range(1, K+1): #K = 1
        for _ in range(len(qq[i])):
            xy = qq[i].pop(0)
            x, y = xy[0], xy[1]
            for f in range(4):
                nx, ny = x + dx[f], y + dy[f]
                #1. 범위에 맞고 and 0이면 -> 증식 
                #증식하고 -> qq에 넣어줘 
                if nx >=0 and ny >=0 and nx<=N-1 and ny <=N-1:
                    if mat[nx][ny] == 0:
                        mat[nx][ny] = i
                        qq[i].append((nx,ny))
                #2. 범위에 맞지않거나, 0이아니면 -> 증식못함 continue 
                else:
                    continue 

                
    sec += 1
    if sec == S:
        print(mat[qx-1][qy-1])
        break 
                
    
            
    
        
