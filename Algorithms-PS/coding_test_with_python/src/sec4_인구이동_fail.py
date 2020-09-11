'''
- (N * N 크기의 땅) (r행 c열)에 있는 나라에 (A[r][c]명)
- 모든 선분은 국경선
-------------------인구이동이 없을떄까지---------------------------
1. 국경선을 공유하는 두 나라의 인구차이가 (L명이상 R명 이하라면) 
    -> 두 나라가 공유하는 국경선을 -> 하루동안 오픈
2. 국경선이 열리면 -> 인구이동 시작
3. 국경선 열려있으면 -> '연합'이라 칭함
4. 연한을 이루고있는 각 칸의 인구수 = (연합의 인구수) / (연합을 이루고있는 칸의 개수)
5. 연합 해체 -> 국경선 닫는다 
===--------------------------------
'''
#
# def dfs(x, y):
#     global ck, city_num, people_num
#     people_num += mat[x][y]
#     ck[x][y] = 1
#     city_num += 1
        
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if nx >= 0 and ny >= 0 and nx <= (N-1) and ny <= (N-1): #범위
#             if ck[nx][ny] == 0: #안간곳이고
#                 if L <= abs(mat[x][y] - mat[nx][ny]) and abs(mat[x][y] - mat[nx][ny]) <= R: #차가맞아
#                     dfs(nx, ny)
#             else:
#                 return
def dfs(x, y):
    global ck, city_num, people_num
    people_num += mat[x][y]
    ck[x][y] = 1
    city_num += 1
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= 0 and ny >= 0 and nx <= (N-1) and ny <= (N-1): #범위
            if ck[nx][ny] == 0: #안간곳이고
                if L <= abs(mat[x][y] - mat[nx][ny]) and abs(mat[x][y] - mat[nx][ny]) <= R: #차가맞아
                    dfs(nx, ny)
            else:
                return

#-------------------------------------------------
#input() 
N, L, R = (map(int, input().split()))
mat = [list(map(int, input().split())) for _ in range(N)]
ck = [[0] * N for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


cnt = 0

while True:
    city_num = 0
    people_num = 0
    ck = [[0] * N for _ in range(N)]

    for a in range(N):
        for b in range(N):
            dfs(a,b)
    #돌면서 ck가 1인 부분은 재분배시켜줘
    done = True
    divided = people_num // city_num
    for i in range(N):
        for j in range(N):
            if ck[i][j] == 1:
                mat[i][j] = divided
                done = False
 
    print(mat)
    print(ck)
    print(people_num)
    print(city_num)
    break 
            
        
# print(people_num)
# print(city_num)
# print(ck)            
        