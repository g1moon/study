# 1 ~ N  까지
#range(idx+1, N+1) -> idx+1 ~ N 
#if idx == M -> 종료 

def dfs(idx, start):
    if idx == M:
#        print(res)
        res_lst.append(res) #이부분...
        return 
    
    else:
        for i in range(start, N+1):
            res[idx] = i
            dfs(idx+1, start + i)
        

if __name__ == "__main__":
    res_lst = [] #종료조건에서의 res를 리스트에 append해 관리하고 싶습니다.
    N,M = map(int, input().split())
    cnt = 0 
    res = [ 0 for i in range(M)]
    dfs(0,1)
     
