import sys
sys.setrecursionlimit(100000)

def go(x,y):
    if x < 0 or y < 0:
        return 0
    
    if dy[x][y] != -1:
        return dy[x][y]
    
    dy[x][y] = max(go(x-1, y), go(x-1, y-1), go(x, y-1)) + mat[x][y]
    return dy[x][y]


if __name__ == "__main__":
    n, m = map(int, input().split())
    mat = [ list(map(int, input().split()))  for _ in range(n)]
    dy = [[-1] * m for _ in range(n)]
    
    print(go(n-1,m-1))
    
    
    