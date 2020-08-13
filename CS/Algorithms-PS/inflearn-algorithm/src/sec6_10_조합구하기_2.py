# 1 ~ N  까지
#range(idx+1, N+1) -> idx+1 ~ N 
#if idx == M -> 종료 

def dfs(idx, start):
    if idx == M:
        print(res)
        return 
    
    else:
        for i in range(start, N+1):
            res[idx] = i
            dfs(idx+1, start + i)
        

if __name__ == "__main__":
    N,M = map(int, input().split())
    cnt = 0 
    res = [ 0 for i in range(M)]
    dfs(0,1)
     