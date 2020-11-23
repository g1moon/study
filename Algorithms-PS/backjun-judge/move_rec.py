import sys
sys.setrecursionlimit(100000)
n,m = map(int, sys.stdin.readline().split())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
d =  [ [-1] * m for _ in range(n)]
print(d)
def go(x,y):
    if x < 0 or y < 0 or x > n-1 or y > m-1:
        return 0
    
    if d[x][y] != -1:
        return d[x][y]
    
    d[x][y] = max(go(x+1, y), go(x+1, y+1), go(x, y+1)) + mat[x][y]
    return d[x][y] 

print(go(0,0))
    
print(mat)
print(d)