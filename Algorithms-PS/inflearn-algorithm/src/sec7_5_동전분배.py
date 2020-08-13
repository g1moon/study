'''
(n개의 동전) 세명한테 나눠줘
적절히 나눠서 -> 세명이 받은 가각의 총액을 계산 
-> 총액이 가장 큰 사람과 가장 작은 사람의 차가 -> 최소
-> 세 사람의 총액은 달라야함 
'''
def dfs(idx, a, b, c):
    global res
    if idx == n:
        ck_lst = [a,b,c]
        max_alp = max(ck_lst)
        min_alp = min(ck_lst)
        diff = max_alp - min_alp
        #save
        if res > diff and a != b and b != c and a != c:
            res = diff
        return
    else:
        dfs(idx+1, a+lst[idx], b, c) 
        dfs(idx+1, a, b+lst[idx], c) 
        dfs(idx+1, a, b, c+lst[idx]) 



if __name__ == "__main__":
    #init
    res = 100000
    #input
    n = int(input()) #동전의 개수 
    lst =  [ int(input()) for _ in range(n)]
    
    #op
    dfs(0,0,0,0)

    #print
    print(res)