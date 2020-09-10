'''
- 연구소의 크기 (N * M)
- 바이러스는 상하좌우로 인전한 칸에 퍼질 수 있음
- 새로 세울 수 있는 벽의 개수는 3개이고 -> 꼭3개 세워야함
'''
#---input()------------
N, M = map(int, input().split())
mat = []
for _ in range(N):
    mat.append(list(map(int, input().split())))
# print(mat)

#----바이러스리스트-------------
virus_lst = []
for i in range(N):
    for j in range(M):
        if mat[i][j] == 2:
            virus_lst.append((i,j))    
# print(virus_lst)
#------------------------------
#북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
#------------------------
def count_safe_area(mat, virus_lst):
    while virus_lst:
        x, y = virus_lst.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:
                continue
            elif mat[nx][ny] == 1:
                continue
            elif mat[nx][ny] == 0:
                mat[nx][ny] = 2
                virus_lst.append((nx,ny))
    cnt = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                cnt += 1
    return cnt 
#----------------------------
from itertools import combinations
import copy
lst = []
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] == 0:
            lst.append((i,j))

prob_case = list(combinations(lst, 3)) #list        
res = 0
for case_tuple in prob_case:
    case_lst = list(case_tuple)
    tmp_mat = copy.deepcopy(mat)
    tmp_virus_lst = copy.deepcopy(virus_lst)
    for i in case_lst:
        a, b = i[0], i[1]
        tmp_mat[a][b] = 1
        
    res = max(res,count_safe_area(tmp_mat, tmp_virus_lst))
        
print(res)















# def dfs(x,y): #입력으로 들어오는 x,y의 부분을 2로바꿔줌
#     global virus_lst, mat
#     #만약 이 부분이 벽이라면 종료하고 , 
#     if mat[x][y] == 1 or x < 0 or y < 0 or x > N-1 or y > M-1:
#         return 
#     #이미 바이러스라면
#     #벽이 아니라면 -> 바이러스로 만들어주고 -> 동서남북으로 나아가 작업
#     elif mat[x][y] == 0:
#         mat[x][y] = 2
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#             if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:
#                 continue 
#             dfs(nx, ny)
# #---------------------
# for _ in range(len(virus_lst)):
#     vx, vy = virus_lst.pop(0)
#     for i in range(4):
#         nvx, nvy = vx + dx[i], vy + dy[i]
#         if mat[nvx][nvy] == 1:
#             continue
#         dfs(nvx, nvy)

# cnt = 0
# for i in range(len(mat)):
#     for j in range(len(mat[0])):
#         if mat[i][j] == 0:
#             cnt += 1
# print(mat)
# print(cnt)
    
    
    
    



    