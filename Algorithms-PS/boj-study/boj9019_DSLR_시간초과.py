# https://www.acmicpc.net/problem/9019
# boj 9019 DSLR
# 시간초과 
'''
- 진짜 모르겠네요 ㅜㅜ 계속 시간초과에요....
'''
from collections import deque
#DSLR
def cal(action, n):
    if action == 'D':
        if n * 2 >  9999:
            return (n*2) % 10000
        else:
            return n * 2
        
    elif action =='S':
        if n == 0:
            return 9999
        else:
            return n-1
        
    elif action =='L' or action =='R':
        
        if action =='L':
            if n >= 1000:
                x = n//1000
                return ((n - (x*1000))*10) + x
            else:
                return n * 10 
        
        else:
            if n >= 1000:
                x = n%10
                return ((n-x) // 10) + (1000*x)
            else:
                x = n%10
                return ((n-x)//10) + (x*1000)
#---------------------
#from, by, cnt 
lst = []
t = int(input())
q = deque()
lst = [ tuple(map(int,input().split())) for _ in range(t)]

def solve(a,b):
    fr_lst, by_lst, cnt_lst = [False]*10000, [False]*10000, [False]*10000
    q.append(a)
    cnt_lst[a] = 0
    
    while q:
        cur = q.popleft()
        for i in ['D','S','L','R']:
            out = cal(i, cur)
            if cnt_lst[out] == False:
                fr_lst[out] = cur #out으로 cur에서  
                by_lst[out] = i  #i에 의해 왔다 
                cnt_lst[out] = cnt_lst[cur] + 1 #현재 횟수에서 1늘어나
                q.append(out)
                 
    while True:
        print(by_lst[b], end ='')
        if fr_lst[b] == a:
            break 
        b = fr_lst[b]    


for a,b in lst:
    solve(a,b)
    print()
    
