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
    rotate_lst.append([x,d])
    
print('n:', N)
print('mat------\n',mat )
print(rotate_lst)
#------------------------------------

#-----rotate method------------------------
#동 남 서 북
#0 1 2 3
def rotate(left_or_right):
    global dir 
    if left_or_right == 'D':
        new_dir = dir + 1
    else:
        new_dir = dir - 1
        
    if new_dir == 4:
        dir = 0
    elif new_dir == -1:
        dir = 3
    else:
        dir = new_dir
#-----------------------------------------