'''
- N * N
- 높이는 서로 다름
- 해당 돌다리 건널 때 -> 돌의 높이 만큼 에너지 소비 
- 현재 지점에서 (오른쪽, 아래만 이동가능)
- (1,1)에서 (N, N) 까지 가는데 드는 에너지의 최소량

'''

'''
solution
1. mat에서 0행과, 0열은 한쪽 방향으로만 진행가능하기떄문에 -> 쭉 적어줌m 
2. 그리고 이중 포문으로 -> (왼쪽에서 오는 경우, 위에서 오는 경우) 에서 작은 거를 할당
'''

n = int(input())

mat = [ list(map(int, input().split())) for _ in range(n)]
ck = [[0] * n for _ in range(n)]


res = 10000000
def dfs(x,y, e):
    global res
    if x == n-1 and y == n-1:
        res = min(res, e)
    if e > res:
        return
    
    ok = False
    if x+1 >= 0 and y >= 0 and x+1 < n and y < n:
        dfs(x+1, y, e + mat[x][y])
        ok = True

    if x >= 0 and y+1 >= 0 and x < n and y < n:
        dfs(x,y+1, e + mat[x][y])
        ok = True
        
    if not ok:
        return 

    
    

dfs(0,0,mat[0][0])
print(res)