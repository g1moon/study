import sys
sys.setrecursionlimit(100000)
n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
dy = [[-1]*n for _ in range(n)]


def rec(x,y):
    l = x-y+1
    
    #길이가 1
    if l == 1: 
        return 1
    elif l == 2: 
        if lst[x] == lst[y]:
            return 1
        else: 
            return 0
    #만약 이미 본 것이면 -> 그 결과를 리턴해라
    if dy[x][y] != -1:
        return dy[x][y]
    
    #만약 양 끝 값, 즉 x,y가 값이 다르면 0으로 넣어둬
    if lst[x] != lst[y]:
        dy[x][y] = 0
        return 0
    #만약 두개의 값이 같으면? -> 한칸씩 이동시켜 다시 확인 
    else:
        dy[x][y] = rec(x+1, y-1)
        return dy[x][y]
    


m = int(sys.stdin.readline())
for _ in range(m):
    s,e = map(int,sys.stdin.readline().split())
    print(rec(s-1,e-1))