'''
- (N * N) 정사각 보드위에서 진행 , 사과가 있는 칸이 있음
- 보드의 상하좌우 끝에는 벽이있음 
- 시작할때 뱀의 좌표는(0,0) -> 뱀길이는1 -> 오른쪽을 향함

- 1. 몸길이를 늘려 머리를 다음칸에 위치함
- 2. 이동한 칸에 사과가 있으면 -> 그 칸의 사과 없어지고 -> 꼬리는 움직이지 않음
- 3. 이동한 칸에 사과가 없으면 -> 몸길이를 줄여 -> 꼬리가 위치한 칸을 비움 (길이변동없음)

input : 사과의 위치와, 뱀의 이동경로
return : 이 게임이 몇 초에 끝나는지 (벽 또는 자기자신의 몸이 닿으면 종료)
'''

#input-----------------------------
N = int(input()) #보드의 크기
K = int(input())#사과의 개수 K 

mat = [ [0] * N for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    mat[x-1][y-1] = 1

rotate_lst = []
L = int(input())
for _ in range(L):
    #x초 끝난 뒤에 왼쪽오른쪽
    input_lst = input().split()
    x, d = input_lst[0], input_lst[1]
    rotate_lst.append([int(x),d])
    
# print('n:', N)
# print('mat------\n',mat )
# print(rotate_lst)
#------------------------------------

#-----rotate method------------------------
#동 남 서 북
#0 1 2 3
def turn(dir, left_or_right):
    if left_or_right == 'D':
        new_dir = dir + 1
    else:
        new_dir = dir - 1
        
    if new_dir == 4:
        return 0
    elif new_dir == -1:
        return 3
    else:
        return new_dir
#-----------------------------------------
#동, 남 서, 북으로 이동할 리스트 
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
#초기값 세팅------------------------------
x, y = 0, 0 #현재 좌표
dir = 0 #시작은 동 
sec = 0 #0초부터 시작
queue = [(x,y)] #뱀 차지하고있는 자리 큐로 관리 
#----------------------------------
while True:
    nx = x + dx[dir]
    ny = y + dy[dir]
    #다음이 내 몸에 닿거나, 범위를 벗어나는경우
    if ((nx,ny) in queue) :
        sec += 1
        break  
    elif nx<0 or ny<0 or nx>(N-1) or ny>(N-1):
        sec += 1
        break    
    
    #1. nxt_head에 사과 없
    if mat[nx][ny] == 0:
        queue.append((nx,ny))
        queue.pop(0)
    #2. nxt_head 사과 있어
    else:
        mat[nx][ny] = 0 #사과 먹었으면 뺴줘야지 
        queue.append((nx,ny))
    
    x = nx
    y = ny 
    
    sec += 1
    if rotate_lst:
        if sec == rotate_lst[0][0]:
            dir = turn(dir, rotate_lst[0][1])
            rotate_lst.pop(0)
        

print(sec)
    