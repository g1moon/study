# 감시피하기
'''
- ( N * N) 복도
- 선생님들은 상하좌우로 감시 진행
- 장애물 뒤는 볼 수 없음
- 상하좌우로는 -> 벽만 없으면 다 볼 수 있음
- 
'''
import sys 
from itertools import combinations
import copy
#-------------------------
def dfs(x,y,dir):
    global print_yes
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    global yes
    #벽이면 중단
    if x < 0 or y < 0 or x > N-1 or y > N-1:
        return 

    elif tmp_mat[x][y] == 'O':
        return 
    #범위도 벗어나지않는 곳이고, 벽도아닌데 -> 학생발견
    if tmp_mat[x][y] == 'S':
        print_yes = False
        return 
    #선생님이거나, X거나 -> 그방향으로 그대로 나아가
    else:
        dfs(x + dx[dir], y + dy[dir], dir)
#---------------------------
#input()
N = int(input())
mat = [ input().split() for _ in range(N)]
# print(mat)
#-----------------------------------
t_coord = []
x_coord = []
for i in range(N):
    for j in range(N):
        if mat[i][j] == 'T':
            t_coord.append((i,j))
        elif mat[i][j] == 'X':
            x_coord.append((i,j))
# print(t_coord)
#------------------------------------


# for one_teacher in t_coord:
#     dfs(one_teacher[0], one_teacher[1], 0)
#     dfs(one_teacher[0], one_teacher[1], 1)
#     dfs(one_teacher[0], one_teacher[1], 2)
#     dfs(one_teacher[0], one_teacher[1], 3) 

    
# print('YES')

#---------------------------------------------------
prob_case = list(combinations(x_coord, 3))

for one_case in prob_case:
    print_yes = True 
    tmp_mat = copy.deepcopy(mat)
    for ixy in one_case:
        ix, iy = ixy[0], ixy[1]
        tmp_mat[ix][iy] = 'O'
        # print(tmp_mat)    
    #--3개벽설치완료
    for one_teacher in t_coord:
        dfs(one_teacher[0], one_teacher[1], 0)
        dfs(one_teacher[0], one_teacher[1], 1)
        dfs(one_teacher[0], one_teacher[1], 2)
        dfs(one_teacher[0], one_teacher[1], 3)
        
    if print_yes:
        print("YES")
        break 

    
        
else:
    print('NO')
