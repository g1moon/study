import sys
sys.setrecursionlimit(100000)

def go(x,y):
    
    if x >= n or y >= m:
        return 0
    
    if dy[x][y] != -1:
        return dy[x][y]
    
    
    #자신의 위치 거 더해주고 -> 가장 큰 쪽으로 켜 
    #키고나서는 -> 거기의 값을 리턴하게 만들어
    dy[x][y] = max(go(x+1, y), go(x+1,y+1), go(x, y+1)) + mat[x][y]
    return dy[x][y]
    


if __name__ == "__main__":
    n, m = map(int, input().split())
    mat = [ list(map(int, input().split()))  for _ in range(n)]
    dy = [[-1] * m for _ in range(n)]
    
    print(go(0,0))
    
    
    