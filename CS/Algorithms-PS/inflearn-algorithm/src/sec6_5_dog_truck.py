def dfs(L, s, ts):
    global lst
    global res
    if L == N:
        if s > res:
            res = s
            return 
    #현재상황에 + (전체합에서 - 지금까지판단해온거들의(쓰던안쓰던))
    #현재상황에 + (남은거(==앞으로 판단할 것))
    #가 현재 res보다 작다면 
    if s > M or (s+(sum(lst)-ts)) < res:
        return 

    else:
        dfs(L+1, s+lst[L], ts + lst[L])
        dfs(L+1, s, ts + lst[L])
    
if __name__ == "__main__":
    M, N = map(int, input().split())
    lst = [ int(input()) for i in range(N)]
    res = -1231241
    dfs(0,0,0)
    print(res)
    
