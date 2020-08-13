#중복순열 구하기
#1부터 N까지의 번호가 적힌 구슬
#중복을 허락해 M번 뽑아 일렬로 나열 

def dfs(idx):
    global cnt 
    if idx == M:
        # print( " ".join(map(str, res)))
        cnt += 1
        return 
    else:
        for i in lst:
            res[idx] = i
            dfs(idx+1)
        

    

if __name__ == '__main__':
    
    N,M = map(int, input().split())
    cnt = 0 
    #1부터 n까지
    lst = [i  for i in range(1, N+1)]
    res = [0 for i in range(M)]
    dfs(0)
    print(cnt)
    