# https://www.acmicpc.net/problem/10974
# boj 10974 S3 순열  
# <메모리 : 125580, 시간 184>
'''
문제 요약
- ck, res 배열 만들고 
- dfs로 탐색하는데 이미 간 곳이면 -> continue 
- dfs로 다음 idx로 넘어가기 전에 ck해주고, res에 값 넣어줌 
'''
n = int(input())
lst = [ i for i in range(1, n+1)]
ck = [0] * n #idx에 잇는 것 사용
res = [-1] * n 

def dfs(idx):
    if idx == n:
        print(' '.join(list(map(str,res))))
        return 
    
    for i in range(n):
        if ck[i] == 1: continue 
        
        ck[i] = 1
        res[idx] = lst[i]
        dfs(idx + 1)
        ck[i] = 0 
        
dfs(0)
    