n, m = map(int, input().split())

ck = [ [0]*m for _ in range(n)]
x, y, dir = map(int, input().split())
ck[x][y] = 1

mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#
def turn_left():
    global dir
    if dir == 0:
        dir = 3
    elif dir == 1:
        dir = 0
    elif dir == 2:
        dir = 1
    elif dir == 3:
        dir = 2
        
#######
cnt = 1
turn_cnt = 0
while True:
    turn_left()
    nx = x + dx[dir]
    ny = y + dy[dir]
    
    #회전 후 정면에 가보지 않은 곳이 있으면 이동
    if ck[nx][ny] == 0 and mat[nx][ny] == 0:
        ck[nx][ny] = 1
        cnt += 1
        x = nx
        y = ny 
        turn_cnt = 0 #다시 0으로 잡아줘 
        continue 
    #앞이 1이면 계쏙 여기 걸림
    #가본 곳이거나, 바다면 -> 그냥 회전만하고 -> 좌표는 업데이트하지마 
    else:
        turn_cnt += 1
    
    if turn_cnt == 4:
        #4방향 모두 돌았는데 전부 갈 수 없으면 
        nx = x - dx[dir]
        ny = y - dy[dir] 
        #이동하는데, 새로운 좌표가 1이면 -> break
        #1이 아니면 -> 뒤로 이동하고 -> 안들린곳이면 1증가
        if mat[nx][ny] == 0:
            x = nx
            y = ny
            if ck[x][y] == 0:
                cnt += 1
                ck[x][y] = 1
            turn_cnt = 0
        else: #1인경우
            print(cnt)
            break  