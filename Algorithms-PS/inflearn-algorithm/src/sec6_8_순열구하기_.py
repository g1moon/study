#1~N 구슬
#M개를 뽑아 일렬로 나열하는 방법 모두 
def dfs(idx):
    global cnt
    if idx == m:
        print(res)
        cnt += 1
        return
    else:
        for i in range(1, n+1):
            if i in res[:idx]:
                # dfs(idx + 1)
                pass
            else:
                res[idx] = i 
                dfs(idx + 1)
            
    


if __name__ == "__main__":
    cnt = 0
    n,m = map(int, input().split())
    lst = [ i for i in range(1,n+1)]
    res = [ 0 for i in range(m)]
    dfs(0)
    print(cnt)
    