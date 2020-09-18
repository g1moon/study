from collections import deque

# 땅의 크기(N), L, R 값을 입력받기
n, l, r = map(int, input().split())

# 전체 나라의 정보(N x N)를 입력 받기
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
 
#특정 위치에서 출발 -> 모든 연합을 체크한 뒤에 -> 데이터 갱신

def process(x, y, idx):
    #(x,y)와 연결된 나라 정보를 담는 리스트
    united = []
    united.append((x,y))
    
    #BFS로 큐 사용
    queue = deque()
    
    #초기화작헙
    queue.append((x,y))
    ck[x][y] = 1 #현재 연합의 번호 할당
    summ = mat[x][y] #현재 연합의 전체 인구수 
    cnt = 1 #현재 연합의 국가수 
    
    #큐가 빌때까지 
    while queue:
        x, y = queue.popleft()
        #4방향
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #바로 옆에있는 나라 확인해서 ->
            if 0 <= nx < n and 0 <= ny < n and ck[nx][ny] == 0:
                #옆에있는 나라와 인구차이가 맞다면
                if l <= abs(mat[nx][ny] - mat[x][y]) <= r:
                    queue.append((nx,ny))
                    #연합에 추가------------
                    ck[nx][ny] = 1 #체크해주고 
                    summ += mat[nx][ny] #더해주고 
                    cnt += 1#연합수 증가
                    united.append((nx,ny)) 
                    
    #연합 국가끼리 인구를 분해
    for i, j in united:
        mat[i][j] = summ // cnt
    
#_-----------------------------
total_cnt = 0
#더이상 인구이동 안할떄까지
while True:
    ck = [[0] * n for _ in range(n)]
    idx = 0
    
    done = True
    for i in range(n):
        for j in range(n):
            print('sibal')
            if ck[i][j] == 0: #처리되지 않은 나라가 있으면 -> 거기에서 처리해주고 
                process(i, j, idx) #한포인트 처리하고 
                idx += 1 #1늘려주고 
    #모든 인구의 이동이 끝나면
    if idx == n*n:
        break 
    total_cnt += 1
    
print(total_cnt)
            
        
    
    
    

