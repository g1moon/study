# 1 ~ N  까지
#range(idx+1, N+1) -> idx+1 ~ N 
#if idx == M -> 종료 

def dfs(idx):
    global cnt
    if idx == M:
        # print(res)
        cnt += 1
        return 
    
    
    for i in range(res[idx-1]+1, N+1):
        res[idx] = i
        dfs(idx+1)
        

if __name__ == "__main__":
    N,M = map(int, input().split())
    cnt = 0 
    res = [ 0 for i in range(M)]
    dfs(0)
    print(cnt)
    
    