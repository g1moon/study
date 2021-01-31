#https://www.acmicpc.net/problem/7562
#boj 7562(S2) 나이트의 이동
#<메모리 : 139684, 시간 : 312>

'''
- bfs
- 나이트는 방향 8개로 나아갈 수 있음 (dx, dy)
- 나아가는 방향의 범위가 맞다면 -> 현재 거리에서 + 1해서 넘겨줌
'''

from collections import deque
dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]

def bfs(x,y):
    #체크 
    ck[x][y] = 1 
    
    #큐에 넣고 
    queue.append( (x,y) )
    
    while queue:
        #큐에서 뺴고 
        cur_x, cur_y = queue.popleft()
        
        #맞으면 -> -1해서 리턴 
        if cur_x == dest_x and cur_y == dest_y:
            return ck[cur_x][cur_y]-1
        
        #아니면 -> 8방향으로 나아가기(범위체크)
        for d in range(8):
            nx, ny = cur_x + dx[d], cur_y + dy[d]
            
            if (0 <= nx < i) and (0 <= ny < i) and (ck[nx][ny] ==0):
                #범위가 맞으면 -> 현재에서 1더해줌 
                ck[nx][ny] = ck[cur_x][cur_y] + 1
                #큐에추가 
                queue.append( (nx,ny))
            

t = int(input())
for _ in range(t):
    i = int(input())
    now_x, now_y = map(int, input().split())
    dest_x, dest_y = map(int, input().split())
    ck = [ [0] * i for _ in range(i)]
    
    queue = deque()
    
    print(bfs(now_x, now_y))