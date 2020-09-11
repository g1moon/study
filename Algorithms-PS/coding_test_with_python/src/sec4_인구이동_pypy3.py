import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N, L, R = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
check = [[False]*N for _ in range(N)]
moving = [[False]*N for _ in range(N)]
cnt = 0

'''
----------------------------
dfs호출하면 
->
1. 체크
2. 해당 좌표 인구 설정 
3. 4방향으로 나아가는데 -> 
    - 범위가 맞지 않으면 올리고
    - 체크가 안되어있고, 조건 맞으면 -> moving에 체크해주고 -> cnt늘려주고 -> 
    - 인구 += dfs(nx,ny)로 
----------------------------
migrate(인구
- 전체 돌면서 moving에 체크된 좌표의 인구를 수정
- 수정하고 -> moving을 꺼줘 
-----------------------------

'''
def dfs(x, y):
    global cnt
    check[x][y] = True
    population = a[x][y]
    for dx, dy in (-1, 0), (0, 1), (1, 0), (0, -1):
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if not check[nx][ny] and L <= abs(a[nx][ny]-a[x][y]) <= R:
            moving[nx][ny] = True
            cnt += 1
            print('----',nx, ny)
            population += dfs(nx, ny)
    return population

def migrate(p):

    print(moving)
    for i in range(N):
        for j in range(N):
            if moving[i][j]:
                print('###', a)
                a[i][j] = p
                moving[i][j] = False

def solve():
    global check, cnt
    ans = 0
    while True:
        moved = False
        check = [[False]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if not check[i][j]: #체크가 안되어있으면 -> dfs켜줘
                    cnt = 1
                    p = dfs(i,j)
                    population = p // cnt
                    
                    #1보다 크면 이동
                    if cnt > 1:
                        a[i][j] = population #시작부분을 나눠진 인구로 
                        migrate(population)
                        moved = True
        
        
        if moved:
            ans += 1
        else:
            break
    print(ans)

solve()
