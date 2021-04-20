'''
- 문제를 완전 잘못 이해함 
- 새로 짜야함.. 
- 테두리 하나씩 왼쪽으로 돌려야 하는데 전체를 돌려버림.
'''
n, m, r = map(int, input().split())
mat = []
ck = [[False] * m for _ in range(n)]
flatList = []

for _ in range(n):
    mat.append(list(map(int, input().split())))
    
def scanAround(start):
    #오른쪽 -> 아래 -> 왼쪽 -> 위 
    nx, ny = start[0], start[1]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    flatList.append(mat[nx][ny])
    ck[nx][ny] = True
    for i in range(4):
        while True:
            nx += dx[i]
            ny += dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                nx -= dx[i]
                ny -= dy[i]
                break 
            
            if ck[nx][ny]:
                break
            
            flatList.append(mat[nx][ny])
            ck[nx][ny] = True
            
    
#-----------------------------
start = (0,0)
while True:
    x, y = start[0], start[1]
    print(x,y)
    if ck[x][y] == True:
        break 
    scanAround(start)
    start = (x+1, y+1)
    
#rotate
rotatedList = flatList[r%(n*m):] + flatList[:r%(n*m)]
print(rotatedList)
# print('-------------')
# for i in range(0, len(rotatedList)-2, m):
#     print(*rotatedList[i:i+m])

                
    
    


    