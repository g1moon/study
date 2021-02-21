# https://www.acmicpc.net/problem/132
# boj 1325 S3 스타트와 링크 
# <메모리 : 129196, 시간 744>
'''
- 축구를 하기 위해 모인 사람 n명(짝수)
- n/2 명으로 이루어진 팀으로 나눠 
- 1~n 번 -> 
- 각팀의 능력치를 최소로 
'''
def dfs(idx, fir, sec):
    global res 
    if idx == n:
        if len(fir) != n//2:
            return 
        
        if len(sec) != n//2:
            return 
        
        #두 개의 리스트 길이가 모두 같음
        t1, t2 = 0, 0 
        
        for i in range(len(fir)):
            for j in range(len(sec)):
                a, b = fir[i], fir[j]
                c, d = sec[i], sec[j]
                t1 += mat[a][b]
                t2 += mat[c][d]
                
        res = min(res, abs(t1-t2))
    
    if len(fir) > n//2 or len(sec) > n//2 : return 
    
    dfs(idx+1, fir+[idx], sec)
    dfs(idx+1, fir, sec + [idx])
    
n = int(input())
mat = [ list(map(int, input().split())) for _ in range(n)]
res = float('inf')
dfs(0, [], [])
print(res)
    
    
   
    
    
        
        
    

    



