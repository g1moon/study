'''
- 상하좌우 숫자보다 크면 -> '봉우리 지역' 
- 봉우리 지역의 개수는
'''

n = int(input())
mat = [ list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnt = 0
for x in range(n):
    for y in range(n):
        highest = True        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue 
            
            if mat[x][y] <= mat[nx][ny]:
                highest = False
                break
        
        if highest:
            cnt +=1
print(cnt)
            
            
        
        
    
    
        