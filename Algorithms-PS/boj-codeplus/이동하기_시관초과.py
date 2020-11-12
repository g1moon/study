

def dfs(x,y, score):
    global ans
    # print(x,y)
    score += mat[x][y]
    if x == n-1 and y == m-1:
        ans = max(ans, score)
        return 
    
    dx = [1, 0, 1]
    dy = [0, 1, 1]
    for i in range(3):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= 0 and ny >= 0 and nx <= n-1 and ny <= m-1:
            dfs(nx, ny, score)
            


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    mat = [ list(map(int,input().split())) for _ in range(n)]
    ans = 0 
    
    dfs(0,0,0)
    
    print(ans)
        
    
