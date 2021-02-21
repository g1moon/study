# https://www.acmicpc.net/problem/132
# boj 1325 S3 스타트와 링크 
# <메모리 : 129196, 시간 744>
'''
- (n*m)
- 벽 or 빈칸 
- 청소기 바라보는 방향 -> 동, 서, 남, 북 
- r: 북쪽으로 떨어진 칸의 개수 
- c: 서쪽으로 떨어진 칸의 개수 
- d: 0, 1, 2, 3 (북, 동, 남, 서)

- 현재 위치 청소 
- 현재 방향을 기준으로 왼쪽보고 -> 청소 안 했으면 -> 회전 -> 전진
-                        -> 

'''
import sys
input = sys.stdin.readline



#input-----------
n, m = map(int, input().split())
x, y, d = map(int, input().split())
mat = [ list(map(int, input().split())) for _ in range(n)]

#-------
#현재위치 청소 
def clean(x,y):
    mat[x][y] = 1

#북 동 남 서 
def go_fwd(x, y, d): 
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    nx, ny = x + dx[d], y + dy[d]
    if nx >= 0 and ny >=0 and nx <= n-1 and ny <= m-1: 
        return nx, ny, d
    
    return False,False,False

#남, 서, 북, 동
def go_bwd(x, y, d):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    
    nx, ny = x + dx[d], y + dy[d]
    if nx >= 0 and ny >=0 and nx <= n-1 and ny <= m-1: 
        return nx, ny, d
    
    return False,False,False

def turn_left(x, y ,d):
    if d == 0: 
        return x, y, 3
    return x, y, d-1

def return_left_coord(x,y,d): #돌고 전진한 위치 
    nx, ny, nd = turn_left(x,y,d) #돌고 
    nx, ny, nd = go_fwd(nx, ny, nd)
    return nx,ny, nd


#-------
cnt = 0

while True:
    #step1
    if mat[x][y] == 0:
        clean(x,y)
        cnt += 1

    #step2
    for _ in range(4):
        nx, ny, nd = return_left_coord(x,y,d)
        if nx < 0 or ny < 0 or nx >=n or ny >= m:
            x, y, d = turn_left(x,y,d) #그냥 회전만 
            continue 
        elif mat[nx][ny] == 1:
            x, y, d = turn_left(x,y,d) #벽이니 그냥 회전만 
            continue
        
        elif mat[nx][ny] == 0:
            x, y, d = nx, ny, nd #0있는 곳으로 이동 
            break 
    
    else:
        x, y, d = go_bwd(x, y, d)
        if x == False:
            break 
        
print(cnt)



    


    
        
    

    


    
   
    
    
        
        
    

    



